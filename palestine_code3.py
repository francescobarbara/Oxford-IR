import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

palestine2 = copy.deepcopy(df)
palestine1 = copy.deepcopy(df)
palestine = pd.concat([palestine1, palestine2], axis = 1)
df = pd.read_excel(r"C:\Users\angus\OneDrive\Desktop\IR stuff\Analysis_Palestinians3.xlsx",
                           usecols = 'U')

palestine = pd.concat([palestine, df], axis = 1)

cols_names = palestine.columns



j = 27
x = palestine[cols_names[j]].value_counts()
x = x/sum(x)

y_pos = np.arange(len(x))


plt.figure()    
plt.barh(y_pos, x, align='center', alpha=0.5)
plt.yticks(y_pos, x.keys())
plt.xlabel('Frequecy')
plt.title(cols_names[j])
plt.savefig(str(27))
plt.savefig(str(27), bbox_inches='tight')


palestine.to_csv(r"C:\Users\angus\OneDrive\Desktop\IR stuff\palestine.csv")
