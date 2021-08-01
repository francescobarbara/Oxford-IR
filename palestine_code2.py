
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\angus\OneDrive\Desktop\IR stuff\Analysis_Palestinians.xlsx",
                           usecols = 'D,E,F,M,O,AB,AO,AR,AS')

cols_names = list(df.columns)

for j in range(len(cols_names)):
    print(j)
    print(df[cols_names[j]].unique())
    
df[cols_names[2]] = df[cols_names[2]].replace(['High school', 'High school,University degree', 'university degree'],
                                                ['High School', 'University degree', 'University degree'])
df[cols_names[3]] = df[cols_names[3]].replace(['Palestinian refugee'], ['Palestinian Refugee'])


series = pd.Series(data = [math.nan for i in range(len(df))])

series2 = [math.nan for i in range(len(df))]

for i in range(len(df)):
    try:
        series2[i] = int(df[cols_names[0]][i])
        
    except:
        pass
    
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





for i in range(len(df)):
    if type(df[cols_names[5]][i]) == str:
            
        if df[cols_names[5]][i][0] == 'Y':
            series[i] = 'Yes'
        elif df[cols_names[5]][i][0] == 'N':
            series[i] = 'No'
        
        
df[cols_names[5]] = series


for j in range(len(cols_names)):
    x = df[cols_names[j]].value_counts()
    x = x/sum(x)
    
    y_pos = np.arange(len(x))
    
    
    plt.figure()    
    plt.barh(y_pos, x, align='center', alpha=0.5)
    plt.yticks(y_pos, x.keys())
    plt.xlabel('Frequecy')
    plt.title(cols_names[j])
    plt.savefig(str(18 + j))
    plt.savefig(str(18 + j), bbox_inches='tight')
    
    
    
    
    
    
