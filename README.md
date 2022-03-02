# TFM_NHANES
Prevalencia de Síndrome Metabólico

Para considerar que un individuo presenta síndrome metabólico se tienen que dar 3 de estos 5 requisitos



------------------------------------
**REQUISITO 1**

Waist circumference >88cm for woman y >102cm for man

*BMXWAIST* => 88cm if RIDAGENDR = female

*BMXWAIST* => 102cm if RIDAGENDR = male

-----------------------------------------


**REQUISITO 2**

triglycerides >150mg/dL || medicine for high blood cholesterol

*LBXTR* => 150mg/dL || 

*BPQ090D* = yes

-----------------------------------------

**REQUISITO 3**

Reduced HDL cholesterol || medicine for high blood cholesterol

*LBDHDD* <= 50cm if RIDAGENDR = female

*LBDHDD* <= 40cm if RIDAGENDR = male
||

*BPQ040A* = yes

----------------------------------------

**REQUISITO 4**

Elevated blood pressure || medicine for elevated blood pressure

*BPXSY1* >= 130mmHg systolic ||

*BPXDI1* >= 85mmHg diastolic ||

*BPQ050A* = yes


--------------------------------------

**REQUISITO 5**

Elevated fasting glucose || medicine for elevated glucose

*LBXGLU* >= 100mg/dL ||

*DIQ070* = yes  (oral agents)

voy a prescindir del *DID070* = yes (pills) 

---------------------------------------
