
"""
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
"""



#LIMPIAR VALORES

#CINTURA POR SEXO (req1)
#se rellenan los nan values de hombres con su moda (100)
#se rellenan los nan values de mujeres con su moda (80.5)
ms1112_male = ms1112[ms1112['RIAGENDR']==1]
ms1112_female = ms1112[ms1112['RIAGENDR']==2]
ms1112_male['BMXWAIST'] = ms1112_male['BMXWAIST'].fillna(100)
ms1112_female['BMXWAIST'] = ms1112_female['BMXWAIST'].fillna(80.5)
ms1112 = pd.merge(ms1112_female, ms1112_male, how = 'outer')

#HDL bajo y pastillas para el hdl (req3)
#reemplazamos valores nulos por moda distinguiendo chicos y chicas
#moda chicos = 44 y moda chicas = 52
#reemplazamos las respuestas para que quede en 2 (no) para valores de no sabe, refused y nulos
ms1112_male = ms1112[ms1112['RIAGENDR']==1]
ms1112_female = ms1112[ms1112['RIAGENDR']==2]
ms1112_male['LBDHDD'] = ms1112_male['LBDHDD'].fillna(44)
ms1112_female['LBDHDD'] = ms1112_female['LBDHDD'].fillna(52)

ms1112 = pd.merge(ms1112_female, ms1112_male, how = 'outer')

ms1112['BPQ040A']= ms1112['BPQ040A'].fillna(2)
ms1112['BPQ040A'] = ms1112.BPQ040A.replace({9: 2})


#TRIGLICERIDOS Y PASTILLAS PARA COLESTEROL ALTO (req2)
#reemplazamos valores nulos de triglicéridos con la moda (75)
#reemplazamos las respuestas nulas, los dont know (7) y los refused (9) por no(2)
ms1112['LBXTR'] = ms1112['LBXTR'].fillna(75)

ms1112['BPQ090D'] = ms1112['BPQ090D'].fillna(2)
ms1112['BPQ090D'] = ms1112.BPQ090D.replace({9: 2})


#Presión sanguínea sistolica (116 = mode) y diastolica (68 = mode) elevada. Pastillas (req4)
#reemplazamos nulos por moda
ms1112['BPXSY1']= ms1112['BPXSY1'].fillna(116)

ms1112['BPXDI1']= ms1112['BPXDI1'].fillna(68)

ms1112['BPQ050A']= ms1112['BPQ050A'].fillna(2)
ms1112['BPQ050A'] = ms1112.BPQ050A.replace({9: 2})


#glucosa en ayunas elevada (moda 97) o pastillas para la diabetes (req5)
ms1112['LBXGLU']= ms1112['LBXGLU'].fillna(97)

ms1112['DIQ070'] = ms1112['DIQ070'].fillna(2)
ms1112['DIQ070'] = ms1112.DIQ070.replace({9: 2})

#CONDICIONES Y AÑADIR FILAS DE REQUISITOS

#CONDICION REQUISITO 1

condiciones_REQ1 = [((ms1112['RIAGENDR'] == 2) & (ms1112['BMXWAIST']>= 102)) | ((ms1112['RIAGENDR'] == 1) & (ms1112['BMXWAIST']>= 88)),
                     ((ms1112['RIAGENDR'] == 2) & (ms1112['BMXWAIST']< 102)) | ((ms1112['RIAGENDR'] == 1) & (ms1112['BMXWAIST']< 88)),
                    ]
                                                  
opciones_REQ1 = [1, 0]

ms1112['REQ1'] = np.select(condiciones_REQ1, opciones_REQ1)


#CONDICION REQUISITO 2

condiciones_REQ2 = [(ms1112['LBXTR'] >= 150) | (ms1112['BPQ090D'] == 1),
                     (ms1112['LBXTR'] < 150) | (ms1112['BPQ090D'] == 2) 
                    ]
                                                  
opciones_REQ2 = [1, 0]

ms1112['REQ2'] = np.select(condiciones_REQ2, opciones_REQ2)

#CONDICION REQUISITO 3

condiciones_REQ3 = [((ms1112['RIAGENDR'] == 2) & (ms1112['LBDHDD']<= 50 )) | ((ms1112['RIAGENDR'] == 1) & (ms1112['LBDHDD'] <= 40)) | (ms1112['BPQ040A'] == 1) ,
                     ((ms1112['RIAGENDR'] == 2) & (ms1112['LBDHDD']> 50)) | ((ms1112['RIAGENDR'] == 1) & (ms1112['LBDHDD'] > 40)) | (ms1112['BPQ040A'] == 2),
                    ]
                                                  
opciones_REQ3 = [1, 0]

ms1112['REQ3'] = np.select(condiciones_REQ3, opciones_REQ3)



#CONDICION REQUISITO 4


condiciones_REQ4 = [(ms1112['BPXSY1'] >= 130) | (ms1112['BPXDI1'] >= 85) | (ms1112['BPQ050A'] == 1),
                     (ms1112['BPXSY1'] < 130) | (ms1112['BPXDI1'] < 85) | (ms1112['BPQ050A'] == 2)
                    ]
                                                  
opciones_REQ4 = [1, 0]

ms1112['REQ4'] = np.select(condiciones_REQ4, opciones_REQ4)

#CONDICION REQUISITO 5

condiciones_REQ5 = [(ms1112['LBXGLU'] >= 100) | (ms1112['DIQ070'] == 1),
                     (ms1112['LBXGLU'] < 100) | (ms1112['DIQ070'] == 2)
                    ]
                                                  
opciones_REQ5 = [1, 0]

ms1112['REQ5'] = np.select(condiciones_REQ5, opciones_REQ5)

#SUMA DE REQUISITOS POR FILA
ms1112['REQ_SUM'] = ms1112['REQ1'] + ms1112['REQ2'] + ms1112['REQ3'] + ms1112['REQ4'] + ms1112['REQ5']

#ENCODING METSYM 1 ES QUE TIENE Y 0 ES QUE NO
condiciones_METSYM = [(ms1112['REQ_SUM'] >= 3),
                     (ms1112['REQ_SUM'] < 3)
                    ]
                                                  
opciones_METSYM = [1, 0]

ms1112['MET_SYM'] = np.select(condiciones_METSYM, opciones_METSYM)


#PREVALENCIA EN PORCENTAJE

#porcentaje de los que presentan sindrome metabolico
#porcentaje_METSYM_1112 = 100 * ms1112['MET_SYM'].value_counts() / len(ms1112['MET_SYM'])
#conteo de valores
#ms1112['MET_SYM'].value_counts()
#ms1112.to_csv('ms1112.csv')
