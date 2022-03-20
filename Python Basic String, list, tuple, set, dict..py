#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Removing particular element from list inside a string

l=['sudh','hjggg',355,5+4j,542.54] #list (mutable)

k=l[0].replace('s','v')

l.remove('sudh')
l.insert(0,'k')
l


# In[43]:


#Tuple
t=(1,2,3,4,[5,'ghj','jf',55],(4,5,6,'j','ju')) #tuple (immutable)
y=list(t)
tuple(y)


# In[58]:


#Set
s=(1,1,12,2,4,5,6,4,64,64,64,6)
k=set(s)
print(k)
a = {}
type(a) #dictionary
type(k) #set
list(k)


# In[1]:


#Set
s={4,51,0,45,5,58}
s.add('s')
s.remove(0)
s


# In[3]:


#IMMUTABLE string
a="gjjjddjdj"
b=a.replace('g','k')
print(a,b)


# In[15]:


#Dictionary {Key : Value} pair
d={"key1":5,"key2":51,"key3":495,"key844":['shfgsh',465,46],51:("rfjf",5,56,49,'he')}
d[51][0] #access value using key
(d['key1'])=4 #mutable


# In[2]:


#Dictionary {Key : Value}
d={"key1":5,"key2":51,"key3":495,"key844":['shfgsh',465,46],51:("rfjf",5,56,49,'he',5)}
#d.keys() to get all key
d.values() #to get all values
#d.items() list of key and value in tuple
#d["a"]=45 to add new data


# In[ ]:




