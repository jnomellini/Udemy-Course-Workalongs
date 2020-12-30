#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")


# In[35]:


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
            
    def eat(self):
        print("I am a dog and eating")        

    def bark(self):
        print("WOOF!")
            


# In[36]:


mydog = Dog()


# In[37]:


mydog.who_am_i()


# In[38]:


myanimal = Animal()


# In[39]:


myanimal.who_am_i()


# In[41]:


mydog.eat()


# In[42]:


mydog.bark()


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




