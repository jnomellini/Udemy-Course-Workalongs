#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math


# In[5]:


# help(math)


# In[7]:


value = 4.35


# In[8]:


math.floor(value)


# In[10]:


math.ceil(value)


# In[11]:


round(4.35)


# In[12]:


round(4.5)


# In[13]:


round(5.5)


# In[14]:


math.pi


# In[15]:


from math import pi


# In[16]:


pi


# In[18]:


math.e


# In[19]:


math.inf


# In[20]:


math.nan


# In[ ]:


# Numpy


# In[21]:


math.e


# In[22]:


math.log(math.e)


# In[23]:


math.log(100,10)


# In[24]:


10**2


# In[25]:


math.sin(10)


# In[26]:


math.degrees(pi/2)


# In[27]:


math.radians(180)


# In[28]:


import random


# In[75]:


random.randint(0,100)


# In[86]:


random.seed(101)

random.randint(0,100)


# In[87]:


random.randint(0,100)


# In[126]:


random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))


# In[127]:


mylist = list(range(20))


# In[128]:


mylist


# In[136]:


random.choice(mylist)


# In[152]:


mylist


# In[150]:


# SAMPLE WITH REPLACEMENT 


# In[153]:


random.choice(population=mylist,k=10)


# In[154]:


# SAMPLE WITHOUT REPLACEMENT 


# In[155]:


random.sample(population=mylist,k=10)


# In[156]:


mylist


# In[157]:


random.shuffle(mylist)


# In[158]:


mylist


# In[160]:


random.uniform(a=0,b=100)


# In[161]:


random.gauss(mu=0,sigma=1)


# In[ ]:





# In[ ]:





# In[ ]:




