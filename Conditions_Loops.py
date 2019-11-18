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


# In[ ]:


#Girilen String'i Tersten Yazdırmak
lolo=[input("tersten yazılmasını istediğiniz ifadeyi yazınız:")]
ters=[]
a=1
for x in lolo:         
    duz="{}".format(x)
uzunluk=len(duz)
while uzunluk > a:    
    for y in duz:
        ters.append(y)
        a+=1
lili= list(ters)
lili.reverse()
t=0
while t < uzunluk:
    print(lili[t],end= "", sep="")
    t+=1
    
                   
    


# In[9]:


#verilen sayı kadar fibonacci sayısının toplamı
x=int(input("sayı: "))    #kulannıcıdan sayı girmesi isteniyor
liste=[1,1]               #ilk iki fibonacci sayısı olan 1,1 liste olarak tanımlanıyor
for x in range(2, x+1):   #verilen sayının da dahil olması için x+1'e kadar range alınıyor    
    liste.append(liste[x-1]+liste[x-2])  #her for döngüsünde listenin son elemanına kendisinden önceki iki elemanın çarpımı ekleniyor

   
        
print(liste)

    
        


# In[10]:


#verilen sayı için çarpım tablosu hazırlama
def Carpim(n):
    numbers=[1,2,3,4,5,6,7,8,9]
    for x in numbers:
        print(n,"x",x," = ",n*x)
        
Carpim(int(input("lütfen sayı giriniz:")))
    


# In[1]:


#list comprehension ile 1 den 20 ye kadar te sayıların karesini çift sayıların küpünü içeren liste
liste=[x**2 if x%2 !=0 else x**3 for x in range(20)]
print(liste)


# In[ ]:




