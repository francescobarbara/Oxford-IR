
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\angus\OneDrive\Desktop\IR stuff\ANALYSIS_results-Austria_Germany_For Francesco.xlsx",
                           usecols = 'B,C,D,G,H,I,J,L,M,N,O,P,R,T,U,X,Y')

cols_names = df.columns

series2 = df[cols_names[0]].tolist()
for i in range(len(df)):
    try:
        if series2[i] < 20:
            series2[i] = '< 20'
        elif series2[i] < 25:
            series2[i] = '20-24'
        elif series2[i] < 30:
            series2[i] = '25-29'
        elif series2[i] < 35:
            series2[i] = '30-34'
        elif series2[i] < 40:
            series2[i] = '35-39'
        elif series2[i] < 50:
            series2[i] = '40-49'
        elif series2[i] < 60:
            series2[i] = '50-59'
        else:
            series2[i] = '60+'
    except:
        pass

df[cols_names[0]] = series2

df1 = df[df[cols_names[3]] == 'D']

df2 = df[df[cols_names[3]] == 'Ö']


df = df2
for j in range(len(cols_names)):
    x = df[cols_names[j]].value_counts()
    x = x/sum(x)
    
    y_pos = np.arange(len(x))
    
    
    plt.figure()    
    plt.barh(y_pos, x, align='center', alpha=0.5)
    plt.yticks(y_pos, x.keys())
    plt.xlabel('Frequency')
    plt.title('Ö - ' + cols_names[j])
    plt.savefig(str(j)+'Ö')
    plt.savefig(str(j)+'Ö', bbox_inches='tight')