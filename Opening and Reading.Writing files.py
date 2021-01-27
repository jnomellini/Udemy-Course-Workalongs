#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


f = open('practice.text','w+')
f.write('This is a test string')
f.close


# In[4]:


import os


# In[5]:


os.getcwd() # Get current working directory


# In[6]:


os.listdir('C:\\Users')


# In[7]:


import shutil


# In[13]:


shutil.move('C:\\Users\\janom\\practice.text',os.getcwd())


# In[9]:


os.listdir('C:\\Users\\janom')


# In[10]:


import send2trash


# In[14]:


os.listdir()


# In[15]:


send2trash.send2trash('practice.text')


# In[16]:


os.listdir()


# In[17]:


os.getcwd()


# In[ ]:


file_path = 'C:\\Users\\janom\\Desktop\\Complete-Python-3-Bootcamp-master\\13-Advanced Python Modules\\Datetime'


# In[21]:


for folder, sub_folders,files in os.walk(file_path):
    
    print(f"Currently looking at {folder}")
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f"Subfolder: {sub_fold}")
        
    print('\n')
    print("the files are: ")
    for f in files:
        print(f"\t File: {f}")    print('\n')


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




