#!/usr/bin/env python
# coding: utf-8

# In[1]:


days={"mon":1,"tues":2,"wed":3,"thurs":4,"fri":5,"satur":6,"sun":7}
daylist=list(days.keys())
print(daylist)
print("please select 2 different days from the above list")
ud1=input("1:")
ud2=input("2:")
daylist.remove(ud1)
daylist.remove(ud2)
print(daylist)


# In[20]:



##2.soru
mo=[["Jan",31],["Feb",28],["March",31],["April",31],["May",31],["June",30],["July",31],["Aug",31],["Sept",30],["Oct",31],["Nov",30],["Dec",31]]
print(mo,"\n")
#3.soru
liste=[[mo[0][0],mo[1][0],mo[2][0],mo[3][0],mo[4][0],mo[5][0],mo[6][0],mo[7][0],mo[8][0],mo[9][0],mo[10][0],mo[11][0]],[mo[0][1],mo[1][1],mo[2][1],mo[3][1],mo[4][1],mo[5][1],mo[6][1],mo[7][1],mo[8][1]
,mo[9][1],mo[10][1],mo[11][1]]  ]
print(list,"\n")


## 4. soru
fall=["Sept","Oct","Nov"]
winter=["Dec","Jan","Feb"]
spring=["March","April","May"]
summer=["June","July","Aug"]

#5.soru
print(summer,"\n") 
s1=summer[0]
s2=summer[1]
s3=summer[2]

i1=liste[0].index(s1)
i2=liste[0].index(s2)
i3=liste[0].index(s3)
print(i1,"\n")
print(liste[1][i1]+liste[1][i2]+liste[1][i3])






# In[ ]:




