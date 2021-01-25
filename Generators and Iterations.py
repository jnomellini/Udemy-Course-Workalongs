#!/usr/bin/env python
# coding: utf-8

# In[5]:


def create_cubes(n):
    
    for x in range(n):
        yield x**3


# In[6]:


for x in create_cubes(10):
    print(x)


# In[7]:


list(create_cubes(10))


# In[10]:


def gen_fibon(n):
    
    a = 1 
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output


# In[11]:


for number in gen_fibon(10):
    print(number)


# In[12]:


def simple_gen():
    for x in range(3):
        yield x


# In[14]:


for number in simple_gen():
    print(number)


# In[15]:


g = simple_gen()


# In[16]:


g


# In[17]:


print(next(g))


# In[18]:


print(next(g))


# In[19]:


print(next(g))


# In[20]:


print(next(g))


# In[21]:


s = 'hello'


# In[ ]:


for letter in s:
    print(letter)


# In[22]:


next(s)


# In[23]:


s_iter = iter(s)


# In[24]:


next(s_iter)


# In[25]:


next(s_iter)


# In[26]:


next(s_iter)


# In[27]:


next(s_iter)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




