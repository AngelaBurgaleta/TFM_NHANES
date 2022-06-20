print(ms1718.shape)
print(data17_18.shape)
print(ms1718_all.shape)

varsreq= ['SEQN', 'REQ1', 'REQ2', 'REQ3', 'REQ4', 'REQ5', 'MET_SYM']
ms1718_paramerge = ms1718[varsreq]
ms1718_all= pd.merge(data17_18, ms1718_paramerge, on='SEQN')
ms1718_all.to_csv('ms1718_all.csv')

#---------------------------------------------

'''
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

ms1112_all = pd.read_csv(url_ms1718_all)
ms1314_all = pd.read_csv(url_ms1314_all)
ms1516_all = pd.read_csv(url_ms1516_all)
ms1718_all = pd.read_csv(url_ms1718_all)

df_all1715 = pd.merge(ms1718_all, ms1516_all, how = 'outer')
df_all1311 = pd.merge(ms1314_all, ms1112_all, how = 'outer')
df_all = pd.merge(df_all1715, df_all1311, how = 'outer')

print(ms1718_all.shape)
print(ms1516_all.shape)
print(ms1314_all.shape)
print(ms1112_all.shape)
print(df_all1715.shape)
print(df_all1311.shape)
print(df_all.shape)

'''


