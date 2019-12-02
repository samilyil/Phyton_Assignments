#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Fahrenheit-Centigrade Converter
z= None
while z == None:
    x=input("please press 1 for Fahrenheit,2 for Centigrade:")
    C=0      
    F=0
    if int(x)==1:       
        F=input("please write a F degree to convert Centigrade:")     
        C=5/9*(int(F)-132)                                             
        print("F:",F,"-->", "C:",C)                               
    elif int(x) ==2:                                                   
        C=input("please write a C degree to convert Fahrenheit:")     
        F=(9*int(C)+160)/5                                            
        print("C:",C,"-->","F:",F)     
    elif x == "q":
        break
    else :
        continue


# In[1]:


# mirror writing
list1=[input("Please Write Something to Reverse:")]
reverse=[]
a=1
for x in list1:         
    first="{}".format(x)
length=len(first)
while length > a:    
    for y in first:
        reverse.append(y)
        a+=1
list2= list(reverse)
list2.reverse()
t=0
while t < length:
    print(list2[t],end= "", sep="")
    t+=1
    
                   
    


# In[2]:


#Calculating the Fibonacci Numbers by Given Number
x=int(input("Number: "))    
list1=[1,1]               
for x in range(2, x+1):      
    list1.append(list1[x-1]+list1[x-2])  

   
        
print(list1)

    
        


# In[4]:


# Times table for the given number
def Carpim(n):
    numbers=[1,2,3,4,5,6,7,8,9,10]
    for x in numbers:
        print(n,"x",x," = ",n*x)
        
Carpim(int(input("Plese Write a Number to Create a Time Table For it:")))
    


# In[1]:


#calculating to cupe of even numbers and square of odd numbers starting by 0 (Zero)  to 20
liste=[x**2 if x%2 !=0 else x**3 for x in range(20)]
print(liste)


# In[ ]:




