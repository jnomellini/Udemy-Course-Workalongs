#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name  +  "  Says woof!"


# In[4]:


class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name  +  "  Says meow!"


# In[5]:


niko = Dog("niko")
felix = Cat("felix")


# In[9]:


print(niko.speak())


# In[8]:


print(felix.speak())


# In[12]:


for pet in [niko,felix]:
    
    print(type(pet))
    print(pet.speak())


# In[15]:


def pet_speak(pet):
    print(pet.speak())
    


# In[18]:



pet_speak(niko)


# In[19]:


pet_speak(felix)


# In[20]:


class Animal(): #<----- This is an abstract method that doesnt do anything 
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# In[29]:


class Dog(Animal):
    
    def speak(self):
        return self.name + " Says Woof!"


# In[30]:


class Cat(Animal):
    
    def speak(self):
        return self.name + " Says Meow!"


# In[31]:


fido = Dog("Fido")


# In[32]:


isis = Cat("Isis")


# In[34]:


print(fido.speak())


# In[35]:


print(isis.speak())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




