import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
from bambi import Model, Prior
import pymc3 as pm
import pickle

root = "data/"
survNoNA = (pd.read_csv(root+"survCleanWithSameCols.csv", index_col=0)
              .sort_values(["year", "sitecode"])
              .drop(['race7', 'stheight', 'stweight', 'qnobese'], axis=1))
medImpute = pd.read_csv(root+"survSomeNA2017.csv").drop(["Unnamed: 0"], axis=1)
medImpute = medImpute.fillna(medImpute.median())
surv2017 = pd.read_csv(root+"imputed2017.csv").drop(["Unnamed: 0"], axis=1)
surv2017.loc[:, ["sex", "grade", "race4", "qnowt"]] = surv2017[["sex", "grade", "race4", "qnowt"]].round()
surv2017 = (surv2017.apply(lambda col : col.mask(col > medImpute[col.name].max(),
                                                 medImpute[col.name].max()),
                           axis=0)
                    .apply(lambda col : col.mask(col < medImpute[col.name].min(),
                                                 medImpute[col.name].min()),
                           axis=0))

qsAdd = "+".join(surv2017.drop(['carRiskScore', 'sitecode',
                                'age', 'sex', 'grade', 'race4',
                                'bmi', 'qnowt'],axis=1).columns)
formulaImput = 'carRiskScore ~ (1|sitecode) + age + C(sex) + C(grade) + C(race4) + bmi + C(qnowt) +' + qsAdd

# Dropping over 98% and getting 2017
percent98 = survNoNA.carRiskScore.quantile(.98)
dat = surv2017.query("carRiskScore < @percent98")
# adding one because asymptote at 0
dat.loc[:, "carRiskScore"] = dat.loc[:, "carRiskScore"] + 1

# modeling with bambi
model_gamma = Model(formulaImput, dat, family="gamma", link="log")
fitted_gamma = model_gamma.fit(draws=10000, tune=3500, target_accept=0.9)

with open('traceBambiModelImpute.pickle', 'wb') as handle:
        pickle.dump(fitted_gamma, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
fitted_gamma.to_netcdf("BambiModelImpute")
