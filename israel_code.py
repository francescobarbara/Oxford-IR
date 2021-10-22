
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\angus\OneDrive\Desktop\IR stuff\Analysis_Israelis.xlsx",
                           usecols = 'A,B,C,H,I,L,N,P,T,U,V,W,X,Y,Z,AC,AE,AG,AI,AM,AO,AP,AQ,AS,AT,AU')

cols_names = list(df.columns)

for j in range(len(cols_names)):
    print(j)
    print(df[cols_names[j]].unique())    
    
    
df[cols_names[1]] = df[cols_names[1]].replace(['male'], ['Male'])
df[cols_names[2]] = df[cols_names[2]].replace(['High school'], ['High School'])
df[cols_names[4]] = df[cols_names[4]].replace(['No'], ['no'])

series2 = df[cols_names[5]].tolist()
for i in range(len(series2)):
    if type(series2[i]) == str:
        try:
            print('a')
            if series2[i][0] == '1':
                series2[i] = 1
            if series2[i][0] == '2':
                series2[i] = 2
            if series2[i][0] == '3':
                series2[i] = 3
            if series2[i][0] == '4':
                series2[i] = 4
            if series2[i][0] == '5':
                series2[i] = 5
        except:
            print('wrong', series2[i])
df[cols_names[5]] = series2
df[cols_names[5]] = df[cols_names[5]].replace(['2', '4', '3', '5 (very proud)', '1 (not proud)',
                                               'I can not decide', 'I cannot decide'], 
                                              [2, 4, 3, 5, 1,"Can't decide","Can't decide" ])
            
df[cols_names[6]] = df[cols_names[6]].replace(['Lots: culture', 'Not: community', 'no nationalism', 
                                               'Lots: personal', 'Lots: suffering', 'Lots: community'], 
                                              ['Lots: Culture', 'Not: Community', 'No nationalism', 
                                               'Lots: Personal', 'Lots: Suffering', 'Lots: Community'])
df[cols_names[7]] = df[cols_names[7]].replace(['Origin', 'National'], ['origin', 'national'])
df[cols_names[8]] = df[cols_names[8]].replace(['both '], ['both'])
df[cols_names[9]] = df[cols_names[9]].replace(['both-sides'], ['two-sides'])
df[cols_names[12]] = df[cols_names[12]].replace([' no', 'no '], 'no')
df[cols_names[13]] = df[cols_names[13]].replace([' political', ' sectarian'], ['political', 'sectarian'])
df[cols_names[15]] = df[cols_names[15]].replace(['Jewish State'], ['Jewish state'])


series = pd.Series(data = [math.nan for i in range(len(df))])
for i in range(len(df)):
    if type(df[cols_names[14]][i]) == str:
            
        if df[cols_names[14]][i][0] == 'Y':
            series[i] = 'Yes'
        elif df[cols_names[14]][i][0] == 'N':
            series[i] = 'No'
        
df[cols_names[14]] = series

df[cols_names[17]] = df[cols_names[17]].replace(['Jewish '], ['Jewish'])
df[cols_names[19]] = df[cols_names[19]].replace(['No', 'Yes'], ['no', 'yes'])
df[cols_names[21]] = df[cols_names[21]].replace(['No', 'Yes'], ['no', 'yes'])
df[cols_names[22]] = df[cols_names[22]].replace(['No', 'Yes'], ['no', 'yes'])
df[cols_names[23]] = df[cols_names[23]].replace(['No', 'Yes'], ['no', 'yes'])



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



for j in range(len(cols_names)):
    x = df[cols_names[j]].value_counts()
    x = x/sum(x)
    
    y_pos = np.arange(len(x))
    
    
    plt.figure()    
    plt.barh(y_pos, x, align='center', alpha=0.5)
    plt.yticks(y_pos, x.keys())
    plt.xlabel('Frequency')
    plt.title(cols_names[j])
    plt.savefig(str(j))
    plt.savefig(str(j), bbox_inches='tight')