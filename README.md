# STATS 551 Project

- [data](https://github.com/brodyee/STATS551_Project/tree/main/data): Contains all data files
   - [sitecodeToSitename.csv](https://github.com/brodyee/STATS551_Project/blob/main/data/sitecodeToSitename.csv): Has the conversion from sitecode to sitename.
   - [survCleanWithSameCols.csv](https://github.com/brodyee/STATS551_Project/blob/main/data/survCleanWithSameCols.csv): Has years 2005 to 2019 with only the columns that are common between all of them.
   - [survCleanWithSomeNA](https://github.com/brodyee/STATS551_Project/blob/main/data/survCleanWithSomeNA.csv): Has years 2005 to 2019 with questions that dont have a lot of missing values.
- [eda](https://github.com/brodyee/STATS551_Project/tree/main/eda): Has each persons eda files
   - [andrewsEDA.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/eda/andrewsEDA.ipynb): Cleaning of datasets and basic EDA. 
   - [brodysEDA.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/eda/brodysEDA.ipynb): *QUICK SUMMARY*
   - [jamesEDA.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/eda/jamesEDA.ipynb): *QUICK SUMMARY*
- [modeling](https://github.com/brodyee/STATS551_Project/tree/main/modeling): Has each persons modeling files
   - [andrewsModeling.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/modeling/andrewsModeling.ipynb): Runs Gibbs sampler used to impute missing data. Analyzes posterior distributions, reports parameter summaries, model checking. 
   - [bambiMedImpute.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/bambiMedImpute.ipynb): *QUICK SUMMARY*
   - [bambiModelImpute.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/bambiModelImpute.ipynb): *QUICK SUMMARY*
   - [bambiNoNA.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/bambiNoNA.ipynb): *QUICK SUMMARY*
   - [brodysModeling.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/modeling/brodysModeling.ipynb): *QUICK SUMMARY*
   - [jamesModeling.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/modeling/jamesModeling.ipynb): *QUICK SUMMARY*
   - [noMissingDataScript.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/noMissingDataScript.ipynb): *QUICK SUMMARY*
   - [noMissingDataScriptExpMH.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/noMissingDataScriptExpMH.ipynb): *QUICK SUMMARY*
- [report](https://github.com/brodyee/STATS551_Project/tree/main/report): Contains proposal and final report files

---
# Literature Review
1. [Python Package Bambi](https://bambinos.github.io/bambi/main/_modules/bambi/models.html#Model.fit)
2. [Python Package pymc3](https://docs.pymc.io/en/v3/api.html)
3. [Bayesian inference for generalized linear mixed models](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2883299/pdf/kxp053.pd)
