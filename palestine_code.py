import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r".\Analysis_Palestinians.xlsx",
                           usecols = 'I,L,Q,S,W,X,Y,Z,AA,AE,AG,AI,AK,AL,AQ,AU,AV,AW')

cols_names = list(df.columns)









#
df[cols_names[1]] = df[cols_names[1]].replace(['No', 'Yes, Jerusalem'],['no', 'yes, Jerusalem'])
df[cols_names[0]] = df[cols_names[0]].replace(['gaza'],'Gaza')
df[cols_names[2]] = df[cols_names[2]].replace(['lots: nationalism', 'No nationalism', 'not: politics', 
                                               'lots: community', 'Not: Politics', 'lots: resistance'],
                                              ['Lots: nationalism', 'Not: nationalism', 'Not: politics', 
                                               'Lots: community', 'Not: politics', 'Lots: resistance'] )
df[cols_names[3]] = df[cols_names[3]].replace(['origin', 'safety'],['Origin', 'Safety'])
df[cols_names[5]] = df[cols_names[5]].replace(['one sides Israel'],'one side Israel')
df[cols_names[6]][df[cols_names[6]] != 'yes'] = 'no'
df[cols_names[7]][df[cols_names[7]] != 'yes'] = 'no'
df[cols_names[9]] = df[cols_names[9]].replace(['islamic', 'Islamic '], ['Islamic', 'Islamic'])
df[cols_names[10]] = df[cols_names[10]].replace(['islamic', 'Islamic ', 'Secular ', 'secular'], 
                                                ['Islamic', 'Islamic', 'Secular', 'Secular'])
df[cols_names[11]] = df[cols_names[11]].replace(['pluralistic', 'Arabs'],['Pluralistic', 'Arab'])
df[cols_names[12]] = df[cols_names[12]].replace(['one state','one-state', 'two-states', 'open'], 
                                                ['One-state', 'One-state', 'Two-states', 'Open'])
df[cols_names[13]][df[cols_names[13]] != 'No'] = 'Yes'
df[cols_names[15]][df[cols_names[15]] != 'yes'] = 'no'

for j in range(len(cols_names)):
    x = df[cols_names[j]].value_counts()
    x = x/sum(x)
    
    y_pos = np.arange(len(x))
    
    
    plt.figure()    
    plt.barh(y_pos, x, align='center', alpha=0.5)
    plt.yticks(y_pos, x.keys())
    plt.xlabel('Frequecy')
    plt.title(cols_names[j])
    plt.savefig(str(j))
    
    





df[cols_names[10]].unique()

x.keys()
len(cols_names)
