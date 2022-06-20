#imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
%matplotlib inline 



url_ms1718_all = 'https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/METSYM_prevalence/ms1718_all.csv'
url_ms1516_all = 'https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/METSYM_prevalence/ms1516_all.csv'
url_ms1314_all = 'https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/METSYM_prevalence/ms1314_all.csv'
url_ms1112_all = 'https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/METSYM_prevalence/ms1112_all.csv'
url_ms1112 = 'https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/METSYM_prevalence/ms1112.csv'
url_ms1516 = 'https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/METSYM_prevalence/ms1516.csv'
url_data11_12 = "https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/download_data/merged/nhanes_2011_2012.csv"
url15_16 = "https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/download_data/merged/nhanes_2015_2016.csv"


ms1112_all = pd.read_csv(url_ms1112_all)
ms1314_all = pd.read_csv(url_ms1314_all)
ms1516_all = pd.read_csv(url_ms1516_all)
ms1516 = pd.read_csv(url_ms1516)
ms1718_all = pd.read_csv(url_ms1718_all)
data11_12 = pd.read_csv(url_data11_12)
data15_16 = pd.read_csv(url15_16)
ms1112 = pd.read_csv(url_ms1112)

df_all1715 = pd.merge(ms1718_all, ms1516_all, how = 'outer')
df_all1311 = pd.merge(ms1314_all, ms1112_all, how = 'outer')
df_all = pd.merge(df_all1715, df_all1311, how = 'outer')

print(ms1718_all.shape)
print(ms1516_all.shape)
print(ms1314_all.shape)
print(ms1112_all.shape)
print(' ')
print(ms1112.shape)
print(data11_12.shape)
print(data15_16.shape)
print(ms1516.shape)
print(' ')
print(df_all1715.shape)
print(df_all1311.shape)
print(df_all.shape)


#quitar columna de unname

df_all.drop(df_all.filter(regex="Unname"),axis=1, inplace=True)





