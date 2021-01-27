#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter


# In[2]:


mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3]


# In[3]:


Counter(mylist)


# In[4]:


mylist = ['a','a',10,10,10]


# In[5]:


Counter(mylist)


# In[6]:


Counter('aaaaaaaaaabbbbbbbbbbbdfdfdfdfsfsfsffwerioter')


# In[7]:


sentence = "How many times does each word show up in this sentence with a word"


# In[8]:


sentence.split()


# In[10]:


Counter(sentence.lower().split())


# In[11]:


letter = 'aaaaaabbbbccccccdddddd'


# In[12]:


c = Counter(letter)


# In[13]:


c


# In[16]:


c.most_common(2)


# In[17]:


list(c)


# In[18]:


from collections import defaultdict


# In[19]:


d = {'a':10}


# In[20]:


d


# In[21]:


d['a']


# In[22]:


d['Wrong']


# In[23]:


d = defaultdict(lambda: 0)


# In[24]:


d['CORRECT'] = 100


# In[25]:


d['CORRECT']


# In[26]:


d['WRONG KEY!']


# In[27]:


d


# In[28]:


mytuple = (10,20,30)


# In[30]:


mytuple[0]


# In[31]:


from collections import namedtuple


# In[32]:


Dog = namedtuple('Dog',['age','breed','name'])


# In[33]:


Dog


# In[34]:


sammy = Dog(age=5,breed='Husky',name='Sam')


# In[35]:


type(sammy)


# In[36]:


sammy


# In[37]:


sammy.age


# In[38]:


sammy.breed


# In[40]:


sammy[1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




