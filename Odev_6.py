#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating a 10x10 array of even numbers fromt 1 to 200
import numpy as np

newArray= np.arange(2,202,2).reshape(10,10)
print(newArray)


# In[2]:


#Creating a function which returns an array surrounded by 1's and has all 0's inside according to the given parameters.

def Array(x,y):

    new_array= np.zeros((x,y))
    new_array[0,]=[1]
    new_array[x-1,]=[1]
    new_array[:,0] =[1]
    new_array[:,y-1]= [1]
    print(new_array)
    
Array(5,7)



# In[ ]:




