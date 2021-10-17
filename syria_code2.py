import copy
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


y_pos = np.arange(10)
x = np.array([0.6,0.55,0.68,0.6,0.56,1.0, 1.0,0.47,0.33,0.025])

plt.figure()    
plt.barh(y_pos, x, align='center', alpha=0.5)
plt.yticks(y_pos, [1,2,3,4,5,6,7,8,9,11])
plt.xlabel('Frequency')
plt.title('Question 12, frequency of 1s')
plt.savefig('12_updated')
plt.savefig('12_updated', bbox_inches='tight')



y_pos = np.arange(7)
x = np.array([0.28,0.27,0.55,0.48,0.46,0.35,0.71])

plt.figure()    
plt.barh(y_pos, x, align='center', alpha=0.5)
plt.yticks(y_pos, [1,2,3,4,5,6,7])
plt.xlabel('Frequency')
plt.title('Question 11, frequency of 5s')
plt.savefig('11_updated')
plt.savefig('11_updated', bbox_inches='tight')
