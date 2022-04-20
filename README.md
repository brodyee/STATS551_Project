# STATS 551 Project

- [data](https://github.com/brodyee/STATS551_Project/tree/main/data): Contains all data files
   - [sitecodeToSitename.csv](https://github.com/brodyee/STATS551_Project/blob/main/data/sitecodeToSitename.csv): Has the conversion from sitecode to sitename.
   - [survCleanWithSameCols.csv](https://github.com/brodyee/STATS551_Project/blob/main/data/survCleanWithSameCols.csv): Has years 2005 to 2019 with only the columns that are common between all of them.
   - [survCleanWithSomeNA.csv](https://github.com/brodyee/STATS551_Project/blob/main/data/survCleanWithSomeNA.csv): Has years 2005 to 2019 with questions that dont have a lot of missing values.
   - [survSomeNA2017.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/survSomeNA2017.csv): Has year 2017 with all column with NA
   - [cleanSurv10s.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/cleanSurv10s.csv): Has cleaned survey data after year 2010 
   - [cleanSurvBefore10s.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/cleanSurvBefore10s.csv): Has cleaned surveyed data before year 2010
   - [medianImputeOnYear.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/medianImputeOnYear.csv): Has median imputed data based on Year
   - [medianImputeOnYearAndSite.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/medianImputeOnYearAndSite.csv): Has imputed data based on Year and Site
   - [SADCQFirst200k.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/SADCQFirst200k.csv): Has original data from CDC after 200k
   - [SADCQLast.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/SADCQLast.csv): Has original data from CDC last 200k
   - [SADCQMid200k.csv](https://github.com/brodyee/STATS551_Project/blob/0ccdb35b4628792af634d7cbf3b96f36f0988e5d/data/SADCQMid200k.csv): Has original data from CDC mid 200k
- [eda](https://github.com/brodyee/STATS551_Project/tree/main/eda): Has each persons eda files
   - [andrewsEDA.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/eda/andrewsEDA.ipynb): Cleaning of datasets and basic EDA. 
   - [brodysEDA.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/eda/brodysEDA.ipynb): Cleaning of datasets, create car risk score, make tables for report, and simple EDA on clean data.
   - [jamesEDA.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/eda/jamesEDA.ipynb): Cleaning of datasets, violin distribution plots, numerical and categorical variables summary statistics
- [modeling](https://github.com/brodyee/STATS551_Project/tree/main/modeling): Has each persons modeling files
   - [andrewsModeling.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/modeling/andrewsModeling.ipynb): Runs Gibbs sampler used to impute missing data. Analyzes posterior distributions, reports parameter summaries, model checking. 
   - [bambiMedImpute.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/bambiMedImpute.py): Uses bambi to fit the one year median impute model. Ran on slurm.
   - [bambiModelImpute.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/bambiModelImpute.py): Uses bambi to fit the one year model impute model. Ran on slurm.
   - [bambiNoNA.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/bambiNoNA.py): Uses bambi to fit the one year no impute model. Ran on slurm.
   - [brodysModeling.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/modeling/brodysModeling.ipynb): Sets up over the year model using pymc3 and the one year bambi models. 
   - [jamesModeling.ipynb](https://github.com/brodyee/STATS551_Project/tree/main/modeling/jamesModeling.ipynb): Build a complex random modeling with all two numerical variables having their grouped random effects.
   - [noMissingDataScript.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/noMissingDataScript.py): Over many years model made with pymc3. Ran on slurm.
   - [noMissingDataScriptExpMH.py](https://github.com/brodyee/STATS551_Project/tree/main/modeling/noMissingDataScriptExpMH.py): Over many years model made with pymc3, ran with log link and uses metropolis hastings. Ran on slurm.
- [report](https://github.com/brodyee/STATS551_Project/tree/main/report): Contains proposal and final report files

---
# Literature Review
1. [Python Package Bambi](https://bambinos.github.io/bambi/main/_modules/bambi/models.html#Model.fit)
2. [Python Package pymc3](https://docs.pymc.io/en/v3/api.html)
3. [Bayesian inference for generalized linear mixed models](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2883299/pdf/kxp053.pd)
