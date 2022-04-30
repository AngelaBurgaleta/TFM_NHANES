"""
This script downloads selected data files from the NHANES repository,
extracts selected columns, and merges across files to create one integrated
csv file per wave.
"""

import pandas
import os
from os import path
import pandas as pd
import numpy as np

#17/18: J
#15/16: I
#13/14: H -> falta este
#11/12: G

# The base URL for all NHANES data
base = "https://wwwn.cdc.gov/Nchs/Nhanes"

# DEMO --------------------------------------
# Demographics files
demo = [
    ("2017-2018", "DEMO_J.XPT"),
    ("2011-2012", "DEMO_G.XPT"),
    ("2015-2016", "DEMO_I.XPT"),
    ("2013-2014", "DEMO_H.XPT"),
    
]

# EXAMINATION -------------------------------
# Blood pressure files
bpx = [
    ("2017-2018", "BPX_J.XPT"),
    ("2011-2012", "BPX_G.XPT"),
    ("2015-2016", "BPX_I.XPT"),
    ("2013-2014", "BPX_H.XPT"),
    
    
]

# Body measures files
bmx = [
    ("2017-2018", "BMX_J.XPT"),
    ("2011-2012", "BMX_G.XPT"),
    ("2015-2016", "BMX_I.XPT"),
    ("2013-2014", "BMX_H.XPT"),
]

# LABORATORY ----------------------

# Trigliceryde
trigly = [
    ("2017-2018", "TRIGLY_J.XPT"),
    ("2011-2012", "TRIGLY_G.XPT"),
    ("2015-2016", "TRIGLY_I.XPT"),
    ("2013-2014", "TRIGLY_H.XPT"),
]

#Insulina LBXIN de los datos 2011 y 2012 se encuentra en GLU_G
ins = [
    ("2017-2018", "INS_J.XPT"),
    ("2015-2016", "INS_I.XPT"),
    ("2013-2014", "INS_H.XPT"),

]

# Glucosa a ver que pasa??
glu = [
    ("2017-2018", "GLU_J.XPT"),
    ("2011-2012", "GLU_G.XPT"),
    ("2015-2016", "GLU_I.XPT"),
    ("2013-2014", "GLU_H.XPT"),


]

# HDL cholesterol
hdl = [
    ("2017-2018", "HDL_J.XPT"),
    ("2011-2012", "HDL_G.XPT"),
    ("2015-2016", "HDL_I.XPT"),
    ("2013-2014", "HDL_H.XPT"),
]



# QUESTIONNARIRE --------------------

#Blood pressure and cholesterol
bpq = [
    ("2017-2018", "BPQ_J.XPT"),
    ("2011-2012", "BPQ_G.XPT"),
    ("2015-2016", "BPQ_I.XPT"),
    ("2013-2014", "BPQ_H.XPT"),
]

# Diabetes data documentation
diq = [
    ("2017-2018", "DIQ_J.XPT"),
    ("2011-2012", "DIQ_G.XPT"),
    ("2015-2016", "DIQ_I.XPT"),
    ("2013-2014", "DIQ_H.XPT"),
]

# Health condition
hsq = [
    ("2017-2018", "HSQ_J.XPT"),
    ("2011-2012", "HSQ_G.XPT"),
    ("2015-2016", "HSQ_I.XPT"),
    ("2013-2014", "HSQ_H.XPT"),
]

# Dietary screener questionnaire 
dbq = [
    ("2017-2018", "DBQ_J.XPT"),
    ("2011-2012", "DBQ_G.XPT"),
    ("2015-2016", "DBQ_I.XPT"),
    ("2013-2014", "DBQ_H.XPT"),
]

# Mental health - Depression
dpq = [
    ("2017-2018", "DPQ_J.XPT"),
    ("2011-2012", "DPQ_G.XPT"),
    ("2015-2016", "DPQ_I.XPT"),
    ("2013-2014", "DPQ_H.XPT"),
]

#Physical activity
paq = [
    ("2017-2018", "PAQ_J.XPT"),
    ("2011-2012", "PAQ_G.XPT"),
    ("2015-2016", "PAQ_I.XPT"),
    ("2013-2014", "PAQ_H.XPT"),
]

#Incomes - poverty ratio index
inq = [
    ("2017-2018", "INQ_J.XPT"),
    ("2011-2012", "INQ_G.XPT"),
    ("2015-2016", "INQ_I.XPT"),
    ("2013-2014", "INQ_H.XPT"),
]

#Sleep disorders
slq = [
    ("2017-2018", "SLQ_J.XPT"),
    ("2011-2012", "SLQ_G.XPT"),
    ("2015-2016", "SLQ_I.XPT"),
    ("2013-2014", "SLQ_H.XPT"),
]

# Alcohol use
alq = [
    ("2017-2018", "ALQ_J.XPT"),
    ("2011-2012", "ALQ_G.XPT"),
    ("2015-2016", "ALQ_I.XPT"),
    ("2013-2014", "ALQ_H.XPT"),
]

# Smoking
smq = [
    ("2017-2018", "SMQ_J.XPT"),
    ("2011-2012", "SMQ_G.XPT"),
    ("2015-2016", "SMQ_I.XPT"),
    ("2013-2014", "SMQ_H.XPT"),
]

# Insurance
hiq = [
    ("2017-2018", "HIQ_J.XPT"),
    ("2011-2012", "HIQ_G.XPT"),
    ("2015-2016", "HIQ_I.XPT"),
    ("2013-2014", "HIQ_H.XPT"),
]

# Medical questions
mcq = [
    ("2017-2018", "MCQ_J.XPT"),
    ("2011-2012", "MCQ_G.XPT"),
    ("2015-2016", "MCQ_I.XPT"),
    ("2013-2014", "MCQ_H.XPT"),
]

#19 docs .xpt
#he quitado mcq160m
# Variables to keep
kvar = ["SEQN", "RIAGENDR", "RIDAGEYR", "RIDRETH3", "DMDEDUC2", "BPXSY1", "BPXDI1", "BMXWT", "BMXBMI", 
"BMXWAIST", "BMXHT", "LBXTR", "LBXIN", "LBXGLU", "LBDHDD", "BPQ040A", "BPQ030", "BPQ050A", 
"BPQ090D", "DIQ010","DIQ070", "ALQ130", "HSD010", "DBQ700", "HIQ011", "MCQ080", "MCQ010", 
"MCQ220", "MCQ300C", "DPQ020", "DPQ030", "DPQ040", "DPQ050", "PAQ605", "PAQ620", "PAQ635", "PAQ650", "PAQ665", 
"SMQ020", "INQ020", "INDFMMPC", 'INDFMMPI', "SLQ050"
]
kvar = set(kvar)

waves = [x[0] for x in demo]

# Create the directory structure
for di in "raw", "csv", "merged":
    try:
        os.mkdir(di)
    except FileExistsError:
        pass

    if di == "merged":
        continue

    for wave in waves:
        try:
            os.mkdir(path.join(di, wave))
        except FileExistsError:
            pass

# Download from the NHANES site
for fb in demo, bpx, bmx, alq, smq, hiq, trigly, ins, glu, hdl, mcq, bpq, diq, hsq, dbq, dpq, paq, inq, slq:
    for fi in fb:

        # Download if we don't already have it
        cmd = "wget -N -P %s %s" % (path.join("raw", fi[0]), path.join(base, *fi))
        os.system(cmd)

        # Extract columns of interest and save as csv.
        fname = path.join("raw", *fi)
        data = pd.read_sas(fname)
        cols = [x for x in data.columns if x in kvar]
        da = data.loc[:, cols]
        da.SEQN = da.SEQN.astype(np.int)
        out = path.join("csv", fi[0], fi[1].replace(".XPT", ".csv.gz"))
        da.to_csv(out, index=None, compression="gzip")

# Merge the files within each wave
for wave in waves:

    dfiles = os.listdir(path.join("csv", wave))
    dfiles = [f for f in dfiles if f.endswith(".csv.gz")]
    dfiles = [path.join("csv", wave, f) for f in dfiles]

    data = [pd.read_csv(f) for f in dfiles]

    da = data.pop(0)
    while len(data) > 0:
        da = pd.merge(da, data.pop(0), left_on="SEQN", right_on="SEQN", how="left")

    fname = path.join("merged", "nhanes_" +
    wave.replace("-", "_") + ".csv")
    da.to_csv(fname, index=False)
