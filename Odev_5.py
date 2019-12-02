#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Saving a ".txf" file 
#Calculating the line numbers 
#Saving the first words of each line to a new list

with open("siir.txt","r") as f:
    full= f.read()
    
    lineNums=len(full.splitlines())
    
    linesList=full.splitlines()
    
    wordsListInLines=[]
    
    firstWordsList=[]
    
    for i in range(len(linesList)-1):
        
        wordsListInLines.append(linesList[i].split())
        
print(wordsListInLines,"\n")

for i in range(len(wordsListInLines)):
        
    for x in range(1):
            
        firstWordsList.append(wordsListInLines[i][x]) 
        
with open("Duzenli_Siir","w",encoding="utf8") as f:  
    for i in range(len(firstWordsList)):
        f.write(str(firstWordsList[i]))
        f.write(" ")
        


# In[ ]:


# Checking if a number is prime or not

def primeCheck(num):
    if num > 1 :
        for i in range(2,num):
            if num % 2 == 0:
                print(num,"is not a prime number")
                break
        else: 
            print(num,"is a prime number")
    else: 
        print(num,"is not a prime number")
        
num=int(input("please enter a number to check: "))
primeCheck(num)


# In[ ]:


# Transfering list to list providing that the second list should have each character max once.
list1= [1,2,2,2,3,4,5,6,7]
list2= []

for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
        
print(list2)

