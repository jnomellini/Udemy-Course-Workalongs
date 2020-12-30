#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3]


# In[2]:


len(mylist)


# In[3]:


class Sample():
    pass


# In[4]:


mysample = Sample()


# In[8]:


print(mysample)


# In[30]:


class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")
    


# In[31]:


b = Book('Python Rocks',"Jose",200)


# In[32]:


print(b)


# In[35]:


print(b)


# In[36]:


del b


# In[33]:


str(b)


# In[34]:


len(b)


# In[28]:


del b


# In[37]:


b


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




