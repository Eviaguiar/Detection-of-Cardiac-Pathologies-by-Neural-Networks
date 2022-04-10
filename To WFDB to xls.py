# -*- coding: utf-8 -*-
"""signals_w.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WnozYw_RR45DPObSy2t-wc9LOQT-LA9l
"""

from google.colab import drive
drive.mount('/content/gdrive')

!pip install wfdb

# Commented out IPython magic to ensure Python compatibility.
from IPython.display import display
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import os
import shutil
import posixpath
import pandas as pd
import wfdb
from wfdb import io, plot
from tqdm import tqdm_notebook as tqdm

# Commented out IPython magic to ensure Python compatibility.
# %cd gdrive/Shareddrives/Tesis: ECG e Imágenes sECG/DataBase/ptbdb

data_folder = 'gdrive/Shareddrives/Tesis: ECG e Imágenes sECG/Red 1/data/ptbdb'
db = 'ptbdb'
record_names = io.get_record_list(db)

record_names

lst = [] 
for i in record_names:
  signals, fields = wfdb.rdsamp(i)
  lst.append(fields['comments'][4])   
print(lst)

lista=[]
for i in lst:
  lista.append(i[22:])
print(lista)

selected_labels = ['Healthy control','Myocardial infarction','Bundle branch block','Cardiomyopathy','Dysrhythmia','Others' ]

arr = np.array([['Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Healthy control', 'Healthy control', 'Valvular heart disease', 'Valvular heart disease', 'Myocardial infarction', 'Dysrhythmia', 'Valvular heart disease', 'Myocardial infarction', 'Dysrhythmia', 'Dysrhythmia', 'Dysrhythmia', 'Valvular heart disease', 'Heart failure (NYHA 2)', 'Healthy control', 'Healthy control', 'Healthy control', 'Heart failure (NYHA 3)', 'n/a', 'Myocardial infarction', 'Healthy control', 'Healthy control', 'Heart failure (NYHA 4)', 'n/a', 'Palpitation', 'Cardiomyopathy', 'Cardiomyopathy', 'Myocardial infarction', 'Cardiomyopathy', 'Stable angina', 'Healthy control', 'Dysrhythmia', 'Myocardial infarction', 'n/a', 'Cardiomyopathy', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'n/a', 'n/a', 'Myocardial infarction', 'n/a', 'Dysrhythmia', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Healthy control', 'Dysrhythmia', 'Myocardial infarction', 'Dysrhythmia', 'n/a', 'Healthy control', 'Healthy control', 'Dysrhythmia', 'Myocardial infarction', 'Myocardial infarction', 'Hypertrophy', 'Myocardial infarction', 'n/a', 'Myocardial infarction', 'n/a', 'n/a', 'Healthy control', 'Healthy control', 'Healthy control', 'Cardiomyopathy', 'Dysrhythmia', 'Dysrhythmia', 'Healthy control', 'Healthy control', 'Healthy control', 'Bundle branch block', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Bundle branch block', 'n/a', 'Dysrhythmia', 'n/a', 'n/a', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'n/a', 'n/a', 'Healthy control', 'Myocardial infarction', 'Healthy control', 'Healthy control', 'n/a', 'Dysrhythmia', 'Valvular heart disease', 'Myocardial infarction', 'n/a', 'n/a', 'Stable angina', 'n/a', 'Myocardial infarction', 'n/a', 'Myocardial infarction', 'Unstable angina', 'Myocardial infarction', 'Myocardial infarction', 'Healthy control', 'Healthy control', 'Bundle branch block', 'n/a', 'Cardiomyopathy', 'Cardiomyopathy', 'Bundle branch block', 'Bundle branch block', 'Bundle branch block', 'Bundle branch block', 'Myocardial infarction', 'Bundle branch block', 'Myocardial infarction', 'Bundle branch block', 'Bundle branch block', 'Bundle branch block', 'Hypertrophy', 'Myocardial infarction', 'Hypertrophy', 'Bundle branch block', 'Healthy control', 'Cardiomyopathy', 'Hypertrophy', 'Bundle branch block', 'Dysrhythmia', 'Bundle branch block', 'Bundle branch block', 'Hypertrophy', 'Cardiomyopathy', 'Myocardial infarction', 'Myocardial infarction', 'Valvular heart disease', 'Bundle branch block', 'Myocardial infarction', 'Hypertrophy', 'Bundle branch block', 'Healthy control', 'Healthy control', 'Myocardial infarction', 'Myocardial infarction', 'Cardiomyopathy', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Myocarditis', 'Hypertrophy', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Cardiomyopathy', 'Cardiomyopathy', 'Healthy control', 'Cardiomyopathy', 'Cardiomyopathy', 'Dysrhythmia', 'Myocardial infarction', 'Healthy control', 'Myocardial infarction', 'Cardiomyopathy', 'Healthy control', 'Healthy control', 'Myocardial infarction', 'Healthy control', 'Healthy control', 'Myocardial infarction', 'Myocarditis', 'Myocardial infarction', 'Myocarditis', 'Myocarditis', 'Myocardial infarction', 'Myocardial infarction', 'n/a', 'Healthy control', 'Healthy control', 'n/a', 'n/a', 'n/a', 'Healthy control', 'Healthy control', 'Healthy control', 'Healthy control', 'Myocardial infarction', 'n/a', 'Myocardial infarction', 'Myocardial infarction', 'Healthy control', 'Healthy control', 'Healthy control', 'n/a', 'Dysrhythmia', 'Myocardial infarction', 'Myocardial infarction', 'Cardiomyopathy', 'Cardiomyopathy', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction', 'Myocardial infarction']])
HC=np.where(arr == 'Healthy control')
MI=np.where(arr == 'Myocardial infarction')
BBB=np.where(arr == 'Bundle branch block')
CA=np.where(arr == 'Cardiomyopathy')
DY=np.where(arr == 'Dysrhythmia')
OT1=np.where(arr == 'Hypertrophy')
OT2=np.where(arr == 'Valvular heart disease')
OT3=np.where(arr == 'Myocarditis')
OT4=np.where(arr == 'Stable angina')
OT5=np.where(arr == 'Unstable angina')
OT6=np.where(arr == 'Heart failure (NYHA 4)')
OT7=np.where(arr == 'Heart failure (NYHA 2)')
OT8=np.where(arr == 'Heart failure (NYHA 3)')
OT9=np.where(arr == 'Palpitation')
print(HC[1])
print(MI[1])
print(BBB[1])
print(CA[1])
print(DY[1])
print(OT1[1])
print(OT2[1])
print(OT3[1])
print(OT4[1])
print(OT5[1])
print(OT6[1])
print(OT7[1])
print(OT8[1])
print(OT9[1])

HC=[316,317,329,330,331,335,336,345,363,368,369,379,380,381,385,386,387,389,390,391,392,393,399,400,401,402,403,404,405,408,410,411,426,427,446,462,463,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,493,494,495,496,499,504,507,508,510,511,520,521,525,526,527,528,533,534,535]
MI=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71
,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125
,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197
,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269
,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,320,323,334,342,347,350,351,352,353,354,357,360,361,362,365,371,372,374,376,409,415,420,422,424,425,436
,438,443,455,456,459,464,465,503,505,509,512,514,517,518,529,531,532,538,539,542,543,544,545,546,547,548]
BBB=[388,394,428,432,433,434,435,437,439,440,441,445,449,451,452,458,461]
CA=[340,341,343,349,382,430,431,447,454,466,497,498,500,501,506,540,541]
DY=[321,324,325,326,346,359,364,366,370,383,384,396,413,450,502,537]
OT=[373,442,444,448,453,460,492,318,319,322,327,414,457,491,513,515,516,344,418,423,337,328,332,339]

len(HC) #80*5 =400
len(MI) #368
len(BBB) #17 *21=357 323
len(CA) #17 *21=357 323
len(DY) #16 *23=368 304
len(OT) #24 *15=360 360

healty=[]
for i in HC:
  healty.append(record_names[i])
print(healty)
len(healty)

A=['patient001/s0010_re', 'patient001/s0014lre', 'patient001/s0016lre', 'patient002/s0015lre', 'patient003/s0017lre', 'patient004/s0020are', 'patient004/s0020bre', 'patient005/s0021are', 'patient005/s0021bre', 'patient005/s0025lre', 'patient005/s0031lre', 'patient005/s0101lre', 'patient006/s0022lre', 'patient006/s0027lre', 'patient006/s0064lre', 'patient007/s0026lre', 'patient007/s0029lre', 'patient007/s0038lre', 'patient007/s0078lre', 'patient008/s0028lre', 'patient008/s0037lre', 'patient008/s0068lre', 'patient009/s0035_re', 'patient010/s0036lre', 'patient010/s0042lre', 'patient010/s0061lre', 'patient011/s0039lre', 'patient011/s0044lre', 'patient011/s0049lre', 'patient011/s0067lre', 'patient012/s0043lre', 'patient012/s0050lre', 'patient013/s0045lre', 'patient013/s0051lre', 'patient013/s0072lre', 'patient014/s0046lre', 'patient014/s0056lre', 'patient014/s0071lre', 'patient015/s0047lre', 'patient015/s0057lre', 'patient015/s0152lre', 'patient016/s0052lre', 'patient016/s0060lre', 'patient016/s0076lre', 'patient017/s0053lre', 'patient017/s0055lre', 'patient017/s0063lre', 'patient017/s0075lre', 'patient018/s0054lre', 'patient018/s0059lre', 'patient018/s0082lre', 'patient019/s0058lre', 'patient019/s0070lre', 'patient019/s0077lre', 'patient020/s0062lre', 'patient020/s0069lre', 'patient020/s0079lre', 'patient021/s0065lre', 'patient021/s0073lre', 'patient021/s0097lre', 'patient022/s0066lre', 'patient022/s0074lre', 'patient022/s0149lre', 'patient023/s0080lre', 'patient023/s0081lre', 'patient023/s0085lre', 'patient023/s0103lre', 'patient024/s0083lre', 'patient024/s0084lre', 'patient024/s0086lre', 'patient024/s0094lre', 'patient025/s0087lre', 'patient025/s0091lre', 'patient025/s0150lre', 'patient026/s0088lre', 'patient026/s0095lre', 'patient027/s0089lre', 'patient027/s0096lre', 'patient027/s0151lre', 'patient028/s0090lre', 'patient028/s0093lre', 'patient028/s0108lre', 'patient029/s0092lre', 'patient029/s0098lre', 'patient029/s0122lre', 'patient030/s0099lre', 'patient030/s0107lre', 'patient030/s0117lre', 'patient030/s0153lre', 'patient031/s0100lre', 'patient031/s0104lre', 'patient031/s0114lre', 'patient031/s0127lre', 'patient032/s0102lre', 'patient032/s0106lre', 'patient032/s0115lre', 'patient032/s0165lre', 'patient033/s0105lre', 'patient033/s0113lre', 'patient033/s0121lre', 'patient033/s0157lre', 'patient034/s0109lre', 'patient034/s0118lre', 'patient034/s0123lre', 'patient034/s0158lre', 'patient035/s0110lre', 'patient035/s0119lre', 'patient035/s0124lre', 'patient035/s0145lre', 'patient036/s0111lre', 'patient036/s0116lre', 'patient036/s0126lre', 'patient037/s0112lre', 'patient037/s0120lre', 'patient038/s0125lre', 'patient038/s0128lre', 'patient038/s0162lre', 'patient039/s0129lre', 'patient039/s0134lre', 'patient039/s0164lre', 'patient040/s0130lre', 'patient040/s0131lre', 'patient040/s0133lre', 'patient040/s0219lre', 'patient041/s0132lre', 'patient041/s0136lre', 'patient041/s0138lre', 'patient041/s0276lre', 'patient042/s0135lre', 'patient042/s0137lre', 'patient042/s0140lre', 'patient042/s0347lre', 'patient043/s0141lre', 'patient043/s0144lre', 'patient043/s0278lre', 'patient044/s0142lre', 'patient044/s0143lre', 'patient044/s0146lre', 'patient044/s0159lre', 'patient045/s0147lre', 'patient045/s0148lre', 'patient045/s0155lre', 'patient045/s0217lre', 'patient046/s0156lre', 'patient046/s0161lre', 'patient046/s0168lre', 'patient046/s0184lre', 'patient047/s0160lre', 'patient047/s0163lre', 'patient047/s0167lre', 'patient048/s0171lre', 'patient048/s0172lre', 'patient048/s0180lre', 'patient048/s0277lre', 'patient049/s0173lre', 'patient049/s0178lre', 'patient049/s0186lre', 'patient049/s0314lre', 'patient050/s0174lre', 'patient050/s0177lre', 'patient050/s0185lre', 'patient050/s0215lre', 'patient051/s0179lre', 'patient051/s0181lre', 'patient051/s0187lre', 'patient051/s0213lre', 'patient052/s0190lre', 'patient053/s0191lre', 'patient054/s0192lre', 'patient054/s0195lre', 'patient054/s0197lre', 'patient054/s0218lre', 'patient055/s0194lre', 'patient056/s0196lre', 'patient057/s0198lre', 'patient058/s0216lre', 'patient059/s0208lre', 'patient060/s0209lre', 'patient061/s0210lre', 'patient062/s0212lre', 'patient063/s0214lre', 'patient064/s0220lre', 'patient065/s0221lre', 'patient065/s0226lre', 'patient065/s0229lre', 'patient065/s0282lre', 'patient066/s0225lre', 'patient066/s0231lre', 'patient066/s0280lre', 'patient067/s0227lre', 'patient067/s0230lre', 'patient067/s0283lre', 'patient068/s0228lre', 'patient069/s0232lre', 'patient069/s0233lre', 'patient069/s0234lre', 'patient069/s0284lre', 'patient070/s0235lre', 'patient071/s0236lre', 'patient072/s0237lre', 'patient072/s0240lre', 'patient072/s0244lre', 'patient072/s0318lre', 'patient073/s0238lre', 'patient073/s0243lre', 'patient073/s0249lre', 'patient073/s0252lre', 'patient074/s0239lre', 'patient074/s0241lre', 'patient074/s0245lre', 'patient074/s0406lre', 'patient075/s0242lre', 'patient075/s0246lre', 'patient075/s0248lre', 'patient075/s0327lre', 'patient076/s0247lre', 'patient076/s0250lre', 'patient076/s0253lre', 'patient076/s0319lre', 'patient077/s0251lre', 'patient077/s0254lre', 'patient077/s0258lre', 'patient077/s0285lre', 'patient078/s0255lre', 'patient078/s0259lre', 'patient078/s0262lre', 'patient078/s0317lre', 'patient079/s0256lre', 'patient079/s0257lre', 'patient079/s0263lre', 'patient079/s0269lre', 'patient080/s0260lre', 'patient080/s0261lre', 'patient080/s0265lre', 'patient080/s0315lre', 'patient081/s0264lre', 'patient081/s0266lre', 'patient081/s0270lre', 'patient081/s0346lre', 'patient082/s0267lre', 'patient082/s0271lre', 'patient082/s0279lre', 'patient082/s0320lre', 'patient083/s0268lre', 'patient083/s0272lre', 'patient083/s0286lre', 'patient083/s0290lre', 'patient084/s0281lre', 'patient084/s0288lre', 'patient084/s0289lre', 'patient084/s0313lre', 'patient085/s0296lre', 'patient085/s0297lre', 'patient085/s0298lre', 'patient085/s0345lre', 'patient086/s0316lre', 'patient087/s0321lre', 'patient087/s0326lre', 'patient087/s0330lre', 'patient088/s0339lre', 'patient088/s0343lre', 'patient088/s0352lre', 'patient088/s0413lre', 'patient089/s0344lre', 'patient089/s0355lre', 'patient089/s0359lre', 'patient089/s0372lre', 'patient090/s0348lre', 'patient090/s0356lre', 'patient090/s0360lre', 'patient090/s0418lre', 'patient091/s0353lre', 'patient091/s0357lre', 'patient091/s0361lre', 'patient091/s0408lre', 'patient092/s0354lre', 'patient092/s0358lre', 'patient092/s0362lre', 'patient092/s0411lre', 'patient093/s0367lre', 'patient093/s0371lre', 'patient093/s0375lre', 'patient093/s0378lre', 'patient093/s0396lre', 'patient094/s0368lre', 'patient094/s0370lre', 'patient094/s0376lre', 'patient094/s0412lre', 'patient095/s0369lre', 'patient095/s0373lre', 'patient095/s0377lre', 'patient095/s0417lre', 'patient096/s0379lre', 'patient096/s0381lre', 'patient096/s0385lre', 'patient096/s0395lre', 'patient097/s0380lre', 'patient097/s0382lre', 'patient097/s0384lre', 'patient097/s0394lre', 'patient098/s0386lre', 'patient098/s0389lre', 'patient098/s0398lre', 'patient098/s0409lre', 'patient099/s0387lre', 'patient099/s0388lre', 'patient099/s0397lre', 'patient099/s0419lre', 'patient100/s0399lre', 'patient100/s0401lre', 'patient100/s0407lre', 'patient101/s0400lre', 'patient101/s0410lre', 'patient101/s0414lre', 'patient102/s0416lre', 'patient103/s0332lre', 'patient108/s0013_re', 'patient111/s0203_re', 'patient120/s0331lre', 'patient128/s0182_re', 'patient135/s0334lre', 'patient138/s0005_re', 'patient139/s0223_re', 'patient140/s0019_re', 'patient141/s0307lre', 'patient142/s0351lre', 'patient145/s0201_re', 'patient148/s0335lre', 'patient149/s0202are', 'patient149/s0202bre', 'patient152/s0004_re', 'patient158/s0294lre', 'patient158/s0295lre', 'patient160/s0222_re', 'patient163/s0034_re', 'patient183/s0175_re', 'patient189/s0309lre', 'patient193/s0008_re', 'patient195/s0337lre', 'patient197/s0350lre', 'patient197/s0403lre', 'patient205/s0426_re', 'patient207/s0428_re', 'patient211/s0433_re', 'patient223/s0445_re', 'patient223/s0446_re', 'patient226/s0449_re', 'patient230/s0454_re', 'patient231/s0455_re', 'patient259/s0495_re', 'patient261/s0497_re', 'patient265/s0501_re', 'patient268/s0505_re', 'patient270/s0507_re', 'patient273/s0511_re', 'patient274/s0512_re', 'patient280/s0535_re', 'patient282/s0539_re', 'patient283/s0542_re', 'patient287/s0547_re', 'patient287/s0548_re', 'patient290/s0553_re', 'patient291/s0554_re', 'patient292/s0555_re', 'patient292/s0556_re', 'patient293/s0557_re', 'patient293/s0558_re', 'patient294/s0559_re']
len(A)

import numpy

x=[]
for i in healty:
  signals, fields = wfdb.rdsamp(i)
  signalspre= np.delete(signals, (0,1,2,3,4,5,12, 13,14), axis=1)
  print(np.shape(signalspre))
  
print('done')

a= list(range(60000,115200, 5000))
a

a=[0,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000]
b=[60000,65000,70000,75000,80000,85000,90000,95000,100000,105000,110000,115000,115199]
c=[60000,65000,70000,75000,80000,85000,90000,95000,100000,105000,110000,115000,115173]
d=[60000,65000,70000,75000,80000,85000,90000,95000,100000,105000,110000,115000,120000]
signalsprecordiales=[]
for i in healty:
  signals, fields = wfdb.rdsamp(i)
  signalspre= np.delete(signals, (0,1,2,3,4,5,12, 13,14), axis=1)
  signalspre1= np.delete(signals, (0,1,2,3,4,5,12, 13,14), axis=1)
  w=np.shape(signalspre)
  if w ==(91987, 6)or w ==(96588, 6): #97000,76800,91987
    signalspre=signalspre[a]
    signalsprecordiales.append(signalspre) 
    print(signalspre)
  elif w == (115200, 6): 
    signalspre=signalspre[a]
    signalsprecordiales.append(signalspre) 
    print(signalspre)
    signalspre1=signalspre1[b]
    signalsprecordiales.append(signalspre1) 
    print(signalspre1)
  elif w == (115174, 6): 
    signalspre=signalspre[a]
    signalsprecordiales.append(signalspre) 
    print(signalspre)
    signalspre1=signalspre1[c]
    signalsprecordiales.append(signalspre1) 
    print(signalspre1)
  elif w == (120012, 6):
    signalspre=signalspre[a]
    signalsprecordiales.append(signalspre) 
    print(signalspre)
    signalspre1=signalspre1[d]
    signalsprecordiales.append(signalspre1) 
    print(signalspre1)
  elif w == (38400, 6)or w == (32000, 6):
    print('no')

print('done')

signalsprecordiales

len(signalsprecordiales)

#a= list(range(100, 2100, 100)) #tomo desde el minuto 2 al 4 cada 10 sec (100 a 2100) (2100 4100) (4100 6100) (6100 8100) (8100 10100) (10100 12100) (12100 14100) (14100 16100)
#a= list(range(2100, 4100, 100))
#a= list(range(4100, 6100, 100))
#a= list(range(6100, 8100, 100))
#a= list(range(8100, 10100, 100))
#a= list(range(10100, 12100, 100))
#a= list(range(12100, 14100, 100))
#a= list(range(14100, 16100, 100))
#a= list(range(16100, 18100, 100))
#a= list(range(18100, 20100, 100))
#a= list(range(20100, 22100, 100))
#a= list(range(22100, 24100, 100))
#a= list(range(24100, 26100, 100))
#a= list(range(26100, 28100, 100))
#a= list(range(28100, 30100, 100))
#a= list(range(30100, 32100, 100)) #*******25
#a= list(range(32100, 34100, 100))
#a= list(range(34100, 36100, 100))
#a= list(range(36100, 38100, 100))
#a= list(range(0,130000, 10000)) #******* 17 Y 16 cada 10 segundos
#a=[0,5000,10000,20000,30000,40000,50000,60000]
signalsprecordiales=[]
for i in healty:
  signals, fields = wfdb.rdsamp(i)
  signalspre= np.delete(signals, (0,1,2,3,4,5,12, 13,14), axis=1)
  #signalspre=signalspre[a]
  signalspre=signalspre[a]
  signalsprecordiales.append(signalspre) 
  print(signalspre)
print('done')

len(signalsprecordiales)

cont=1 # 1 
for signalspre in signalsprecordiales:
  data = {'v1': signalspre[:, 0],'v2': signalspre[:, 1],'v3': signalspre[:, 2],
          'v4': signalspre[:, 3],'v5': signalspre[:, 4],'v6': signalspre[:, 5]}

  df = pd.DataFrame(data, columns = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6'])
  #['Healthy control','Myocardial infarction','Bundle branch block','Cardiomyopathy','Dysrhythmia','Others' ]
  writer ='6.Others'+str(cont) +'.xlsx'
  df.to_excel(writer, index=False)
  cont = cont + 1
print('done')
print(cont)

label=signalsprecordiales.index()
#label2=lst(label)

len(lst)

signals, fields = wfdb.rdsamp('patient285/s0544_re')

signals #nop

#len (signals) nopppppppp
#type(signals)
np.shape (signals)

lst = [] 
for i in tqdm(record_names):
    lst.append(fields['comments'][4] )   
print(lst)

signalspre= np.delete(signals, (0,1,2,3,4,5,12, 13,14), axis=1)
signalspre
a= list(range(100, 300, 10)) #tomo desde el minuto 2 al 4 cada 10 sec
signalspre=signalspre[a]
signalspre

a= list(range(100, 300, 10)) #tomo desde el minuto 2 al 4 cada 10 sec
signalsprecordiales=[]
for i in record_names:
  signals, fields = wfdb.rdsamp(i)
  signalspre= np.delete(signals, (0,1,2,3,4,5,12, 13,14), axis=1)
  signalspre=signalspre[a]
  signalsprecordiales.append(signalspre) 
  print(signalspre)

data = {'v1': signalspre[:, 0],
        'v2': signalspre[:, 1],
        'v3': signalspre[:, 2],
        'v4': signalspre[:, 3],
        'v5': signalspre[:, 4],
        'v6': signalspre[:, 5]}
df = pd.DataFrame(data, columns = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6'])
print(df)

df.to_excel('juanito.xlsx', sheet_name='example')

record =  wfdb.rdrecord('patient285/s0544_re')
record = record

wfdb.plot_wfdb(record=record, title='Record patient 285', figsize=(10, 30)) 
# display(record.__dict__)

"""https://www.delftstack.com/api/python-pandas/pandas-dataframe-dataframe.to_excel-function/

"""