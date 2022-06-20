

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#leer de github
url11_12 = "https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/download_data/merged/nhanes_2011_2012.csv"
url13_14 = "https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/download_data/merged/nhanes_2013_2014.csv"
url15_16 = "https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/download_data/merged/nhanes_2015_2016.csv"
url17_18 = "https://raw.githubusercontent.com/AngelaBurgaleta/TFM_NHANES/main/download_data/merged/nhanes_2017_2018.csv"

data11_12 = pd.read_csv(url11_12)
data13_14 = pd.read_csv(url13_14)
data15_16 = pd.read_csv(url15_16)
data17_18 = pd.read_csv(url17_18)

#Dataset para quedarnos con las variables que son relevantes para estudiar la prevalencia de síndrome metabólico, tienen que quedar 12 params
vars_metsym = ["SEQN", "RIAGENDR", "BMXWAIST", "LBXTR", "BPQ090D", "LBDHDD", "BPQ040A", "BPXSY1", "BPXDI1", "BPQ050A", "LBXGLU", "DIQ070"]

ms1718= data17_18[vars_metsym]
ms1516= data15_16[vars_metsym]
ms1314= data13_14[vars_metsym]
ms1112= data11_12[vars_metsym]



