#!/usr/bin/env python
# coding: utf-8

# In[7]:


#PANDAS 1. SORU ÇÖZÜMÜ
import pandas as pd
import numpy as np
import warnings 
import string
warnings.filterwarnings('ignore')

# Defining a function which returns a list of first 10 prime number
def prime(x):
    primeNumbers= []
    for val in range(x):
        if val > 1 :
            for n in range(2,val):
                if (val%n) == 0:
                    break
            else:
                primeNumbers.append(val)
            
    return primeNumbers
            

prime(30) 

# defining a funciton which returns first 10 fibonacci numbers

def fibonacci(x):
    numbers1 = [1,1]
    for i in range(2,x):
        numbers1.append(numbers1[i-1]+numbers1[i-2])
    return numbers1
    
fibonacci(10)

# First 10 letters of alphabet

string.ascii_lowercase
indeks_= list(string.ascii_lowercase[:10])
indeks_ 

df = pd.DataFrame({"Prime Numbers" : prime(30),
                   "Fibonacci Numbers": fibonacci(10)
                  })
df.index=indeks_
df


# In[8]:


#Reading 'train.csv' file
tdf = pd.read_csv("train.csv")
tdf


# In[9]:


# Calculating the average ages of passengers for each gender
e2=tdf.groupby("Sex").mean()["Age"]
e2


# In[10]:


#Listing passengers who are under 30 years 
e3 =tdf.loc[lambda v3: tdf["Age"] < 30]
e3


# In[11]:


# Calculating the Survival Ratio of passengers for each gender who are unders 30 years
ratio= e3[e3["Survived"] == 1]["Sex"].value_counts(1)

femaleRatio = ratio[0]
maleRatio = ratio[1]

print("%", "{:.2f}".format(100*femaleRatio)) 


# In[ ]:





# In[ ]:




