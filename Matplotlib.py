#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')

df = pd.read_csv('heart.csv')

plt.subplot(1,2,1)
plt.bar(df.index, df['age'], color = 'green')

plt.subplot(1,2,2)
plt.bar(df.index, df['thalach'], color = 'blue')

plt.show()


# In[ ]:




