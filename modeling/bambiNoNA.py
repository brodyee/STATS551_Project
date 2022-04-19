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


qsAdd = "+".join(survNoNA.drop(['carRiskScore', 'sitecode', 'year',
                                'age', 'sex', 'grade', 'race4',
                                'bmi', 'qnowt'],axis=1).columns)
formulaImput = 'carRiskScore ~ (1|sitecode) + age + C(sex) + C(grade) + C(race4) + bmi + C(qnowt) +' + qsAdd

# Dropping over 98%
percent98 = survNoNA.carRiskScore.quantile(.98)
dat = survNoNA.query("carRiskScore < @percent98 & year == 2017")

# adding one because asymptote at 0
dat.loc[:, "carRiskScore"] = dat.loc[:, "carRiskScore"] + 1

# modeling with bambi
model_gamma = Model(formulaImput, dat, family="gamma", link="log")
fitted_gamma = model_gamma.fit(draws=10000, tune=3500, target_accept=0.9)

with open('traceBambiNoNA.pickle', 'wb') as handle:
        pickle.dump(fitted_gamma, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
with open('modelBambiNoNA.pickle', 'wb') as handle:
        pickle.dump(model_gamma, handle, protocol=pickle.HIGHEST_PROTOCOL)