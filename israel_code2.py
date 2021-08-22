import copy
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


israel = copy.deepcopy(df)

cols = israel.columns

israel[cols[-1]] = israel[cols[-1]].fillna('no')

j = 25
x = israel[cols_names[j]].value_counts()
x = x/sum(x)

y_pos = np.arange(len(x))


plt.figure()    
plt.barh(y_pos, x, align='center', alpha=0.5)
plt.yticks(y_pos, x.keys())
plt.xlabel('Frequency')
plt.title(cols[j])

plt.savefig('25_updated', bbox_inches='tight')

df = pd.read_excel(r"C:\Users\angus\OneDrive\Desktop\IR stuff\Analysis_Israelis.xlsx",
                           usecols = 'J')

cols_names = df.columns

df[cols_names[0]].unique()

israel = pd.concat([israel, df], axis = 1)
cols_names = israel.columns

j = 26
x = israel[cols_names[j]].value_counts()
x = x/sum(x)

y_pos = np.arange(len(x))


plt.figure()    
plt.barh(y_pos, x, align='center', alpha=0.5)
plt.yticks(y_pos, x.keys())
plt.xlabel('Frequency')
plt.title(cols_names[j])
plt.savefig('26')
plt.savefig('26', bbox_inches='tight')
