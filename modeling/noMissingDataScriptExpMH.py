import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
from bambi import Model, Prior
import pymc3 as pm
import pickle
import multiprocessing as mp
import statsmodels.api as sm

n_jobs = 4

root = "../data/"
survNoNA = pd.read_csv(root+"survCleanWithSameCols.csv", index_col=0).sort_values(["year", "sitecode"])

percent98 = survNoNA.carRiskScore.quantile(.98)
years = [2013, 2015, 2017]

#generate sample from data just for testing
for year in years:
    dat = survNoNA.query("carRiskScore < @percent98 & year == @year")
    dat.loc[:,"carRiskScore"] = dat["carRiskScore"] + 1
    county_idxs, counties = pd.factorize(dat["sitecode"]) # needed for hierarchical model
    
    if year != 2013:
        counties = list(counties)
        newCountiesOrder, deletedCountiesIdx = [], []
        # finds the common counties from the previous years,
        # and what to add and delete
        i = 0
        for i, c in enumerate(coords["county"]):
            if c not in counties:
                deletedCountiesIdx.append(i)
            else:
                newCountiesOrder.append(c)
                counties.remove(c)
            i += 1
        
        newCountiesOrder += counties
        n = len(newCountiesOrder)
        # Updates the post dict to have the right number of counties, and for the new counties
        # it makes the starting point the betaN.
        for k in postDict.keys():
            if "County" in k:
                postDict[k] = [num for i,num in enumerate(postDict[k]) 
                                   if i not in deletedCountiesIdx]
                if "sig" in k:
                    postDict[k] += [postDict["ySig"]] * (n - len(postDict[k]))
                else:
                    postDict[k] += [postDict["beta"+k[10:]]] * (n - len(postDict[k]))
        
        counties = newCountiesOrder       
    coords = {
        "county": counties,
        "obs_id": np.arange(len(county_idxs)),
    }
    with pm.Model(coords=coords) as model:  # model specifications in PyMC3 are wrapped in a with-statement
        
        county_idx = pm.Data("county_idx", county_idxs, dims="obs_id")
    
        # Data Setup
        X = dat.drop(["carRiskScore", "sitecode", "year", "race7"], axis=1)
        catCols = ['age', 'sex', 'grade', 'race4']
        for catCol in catCols:
            X = pd.concat([X.drop(catCol, axis=1),
                             (pd.get_dummies(X[catCol], drop_first=True)
                                .rename(columns=lambda x: catCol+str(x)))],
                            axis=1)
        X.insert(0, "intercept", 1)
        gamma_model = sm.GLM(dat.carRiskScore, X, family=sm.families.Gamma(link=sm.families.links.log()))
        gamma_results = gamma_model.fit()
        coef = gamma_results.params.to_numpy()
        sde = gamma_results.bse.to_numpy()
        
        # Defining betas for mu
        mu_est = 0
        for i, q in enumerate(X.columns):
            if i == 0:
                countyLevel = pm.Normal("betaCounty" + str(i), 0, sigma=1, dims="county")
                q_beta = pm.Normal("beta" + str(i), coef[i], sigma=sde[i]/100)
                mu_est += (q_beta + countyLevel[county_idx]) * X.iloc[:,i]
            else:
                #countyLevel = pm.Normal("betaCounty" + str(i), 1, sigma=10, dims="county")
                q_beta = pm.Normal("beta" + str(i), coef[i], sigma=sde[i])
                mu_est += (q_beta) * X.iloc[:,i]# + countyLevel[county_idx]
        
        # Defining Random Sigma
        #countyLevel = pm.Normal("sigCounty", 0, sigma=1, dims="county")
        ySig = pm.Gamma("ySig", mu=1, sigma=10)
        
        # Define likelihood
        mu = pm.Deterministic("mu", pm.math.exp(mu_est), dims="obs_id")
        likelihood = pm.Gamma(
            "y",
            mu=mu,
            sigma=(ySig),# + countyLevel[county_idx]),
            observed=dat["carRiskScore"], dims="obs_id")
        
    with model:
        if year == 2013:
            trace = pm.sample(draws=10000, chains=4, tune=2000, step=pm.Metropolis(), return_inferencedata=True)
        else:
            trace = pm.sample(draws=10000, chains=4, tune=2000, step=pm.Metropolis(), return_inferencedata=True, start=postDict)
          
    # Saving trace as pickle
    with open('traceExpMH'+str(year)+'.pickle', 'wb') as handle:
        pickle.dump(trace, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    with open('modelExpMH'+str(year)+'.pickle', 'wb') as handle:
        pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # (n_jobs, n samples, num of hierarchies)
    postDict = trace.to_dict()["posterior"]
    for k in postDict.keys():
        postDict[k] = postDict[k].mean(axis=0).mean(axis=0)
