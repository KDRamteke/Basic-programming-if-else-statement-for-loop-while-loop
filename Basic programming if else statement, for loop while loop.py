#!/usr/bin/env python
# coding: utf-8

# In[38]:


#if else statement
print("Enter your income")
income=int(input())
if income < 50000:
    Expenses=income*.9
    Saving=income-Expenses
    print("Expenses",Expenses)
    print("Saving",Saving)
elif income>50000:
    Expenses=income*.7
    Saving=income-Expenses
    print("Expenses",Expenses)
    print("Saving",Saving)
else:
    Expenses=income*.8   
    Saving=income-Expenses
    print("Expenses",Expenses)
    print("Saving",Saving)

        


# In[45]:


#Mark price and cost price
print("Enter your cost price")
cost_price=float(input())

if cost_price>10000:
    mark_price=cost_price*1.5
    discount=mark_price*.3
    selling_price=mark_price-discount
    print("Mark price",mark_price)
    print("Discount",discount,'Selling price',selling_price)
elif cost_price<10000:
    mark_price=cost_price*1.2
    print("Mark price",mark_price)
    print('Your not eligible for discount.',"Selling price",mark_price)
    
else:
    mark_price=cost_price*1.2
    discount=mark_price*.25
    selling_price=mark_price-discount
    print("Mark price",mark_price)
    print("Discount",discount,'Selling price',selling_price)
    
    
    


# In[60]:


study_hour=float(input())
if study_hour>0 and study_hour<=1 :
    print("It take 12 month of time to make transition")
elif study_hour<=10 and study_hour>1:
    print("It take 6 month of time to make transition")
elif study_hour>10:
    print("It take 3 month of time to make transition")
else:
    print("It will be difficult to make transition")
    


# # for loop
#     

# In[1]:


l=[1,2,3,4,5]
for i in l:
    print(i)


# In[67]:


s="skkdj"
for i in c:
    print(i)


# In[68]:


t=('e','g','dfg','dg','gd',[5,9],55,8)
for i in t:
    print(i)


# In[2]:


l=[4,5,8,9,78,46]
for i in l:
    i=i+2  #adding no in list
    print(i)


# In[1]:


l=[4,5,8,9,78,46]
l2=[]
for i in l:
    l2.append(i+2)
print(l2)


# In[19]:


#printing integers value from list and creating list of square of integers value 
integer=[4,5,88,4,6,"jglfds",['eh',84,484,46,46],1,(1,856,'f','4',5),55]
sq=[]
for i in integer:
    if type(i)==int:
        a=i*i
        sq.append(a)
        print(i)
    elif type(i)==list:
        for j in i:
            if type(j)==int :
                b=j*j
                sq.append(b)
                print(j)
    elif type(i)==tuple:
        for k in i:
            if type(k)==int:
                c=k*k
                sq.append(c)
                print(k)
print("Square of integers from given list", sq)


# In[31]:


#Extracting string and creating new string to add all the string
x=[4,5,88,4,6,"jglfds",['eh',84,484,46,46],1,(1,856,'f','4',5),55] 
x1=[]
for i in x:
    if type(i)==str:
        x1.append(i)
        print(i)
    elif type(i)==list:
        for j in i:
            if type(j)==str:
                x1.append(j)
                print(j)
    elif type(i)==tuple:
        for k in i:
            if type(k)==str:
                x1.append(k)
                print(k)
print("New string list -", x1)
#for l in x: ####Note: if same value in list then index will always same ex 4 check it, so use range function.
    
 #   print("Index of ",l,"is",x.index(l)) #printing index 
    
for r in range(len(x)): # range fuction
    
        print("index",r, "for element", x[r])
        


# In[49]:


# enumerate function to print index and value

x=[4,5,88,4,6,"jglfds",['eh',84,484,46,46],1,(1,856,'f','4',5),55]
for i in enumerate(x):
    print("Index and respective value",i)
    


# In[43]:


chrs=['fshdk',55,'fhSD',57,'H']
chlist=[]
for i in chrs:
    if type(i)==str:
        for j in i:
            chlist.append(j)
print(chlist)
            


# # for else statement

# In[3]:


f=['name','emailid','phoneno',"adress"]
for i in f:
    print(i)
else:
    print("if for loop is not going to complete itself then it will come to else")
    


# In[7]:


# break
f=['name','emailid','phoneno',"address"]
for i in f:
    if i=="address":
        break
    print(i)
else:
    print('check list')


# # While statement

# In[1]:


b=1
while b<6:
    print(b)
    b=b+1


# In[14]:


#break
a=1
while a<10:
    print(a)
    if a==4:
        break
    a=a+1


# In[11]:


#continue
a=1
while a<10:
    print(a)
    a=a+1
    if a==4:
        continue
    


# In[29]:


n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*", end='')
    print("\r")
        


# In[31]:


t=(0,5,6,8,854,88,78)
for i in range(len(t)):
    print(i, t[i])


# In[42]:


#printing data in reverse order
t=(0,5,6,8,854,88,78)
for i in range(len(t)-1,-1,-1):
    print(i, t[i])


# In[43]:


len(t)


# In[62]:


#Finding length of tuple, list or string without using len function
t=(0,5,6,8,854,88,78) 
sum=0
for i in t:
    sum=sum+1
    print(sum-1,i) 
    
print("\nlength of tuple is",sum)    

    


# In[4]:


#Extracting data from dictionary

d={"a":46,'f':4,"sdfds":"sd","saf":[45,56,648,"ffd"]}

for i in d:
    print("Key",i, "and its value is",d[i])


# In[5]:


for i in d.items(): #Extracting data from dictionary using function
    print(i)


# In[7]:


#Count no of letter inside the string
l="basic python class"
s=0
for i in l:
    s+=1
print(s)


# In[57]:


l="basic python class" 
for i in range(len(l)-1,-1,-1):
    print((i,l[i]))


# In[30]:


#printing string in reverse order with the help of while
l="basic python class"
i=len(l)-1
while i>=0:
    print(l[i],end='')
    i=i-1


# In[46]:


#which one is vowel
t="ineuron"
v='AaEeIiOoUu'
for i in t:
    if i in v:
        print(i, "Vowel")
    else:
        print(i, "Consonant")
        


# In[85]:


#Pallindrome
p="teyet"
l=p[::-1]
if p==l:
    print(p, "is a pallindrome")
else:
    print(p, "is not a pallindrome")
    
    


# In[104]:


#Pallindrome
p=input()
for i in range(len(p)):
    if p[i]!=p[len(p)-1-i]:
        print("Not a pallindrome")
        break
        
else:
    print("pallindrome")


# In[4]:


d={'india':'in', "canada":"ca",'china':'ch', 'united state':'us'}
dg5=[]
dl5=[]
for i in d:
    if len(i)>5:
        dg5.append(i)
        #print("Greater than 5 chac:",i)
        
    else:
        dl5.append(i)
        #print("Less than 5 chac:",i)
print("Greater than 5 chac:",dg5, "Less than 5 chac:",dl5)
        


# In[28]:


#Maximum value from given dictionary
d={"ineuron":{"a":14,"b":10,"c":4},"course":{"d":45,"e":34,"f":1}}
d_1=[]
for i in d.values():
    #print(i)
    for j in i.values():
        d_1.append(j)
print("maximum value from given dictionary", d_1, "is",max(d_1))
    


        
        


# In[83]:


#Maximum value from given dictionary

d_1={"ineuron":{"a":14,"b":0.100000,"c":4},"course":{"d":45,"e":34,"f":1},"g":34+7j,"h":[100,6,7,8,9,3],"i":(5000,34,2),"k":"sudh","l":88956}
d_2=[]
for i in d_1.values():
    
    if type(i)==dict:  #extracting data from dictionary
        for j in i.values():
            d_2.append(j)
            
            
    elif type(i)==int: #integer value
        d_2.append(i)
        
    elif type(i)==list:  #extracting data from list
        d_2.extend(i)
        
        
    elif type(i)==tuple:  #extracting data from tuple
        d_2.extend(i)
        
    else:
        pass
print(d_2)
print(max(d_2))


    


# In[ ]:





# In[ ]:




