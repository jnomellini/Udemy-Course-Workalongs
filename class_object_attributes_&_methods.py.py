#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3]


# In[3]:


myset = set()


# In[5]:


type(mylist)


# In[42]:


class Dog(): 
    
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal' 
    
    def __init__(self,breed,name): #INIT (a method) is the constructor for a class and be called automatically, #SELF represents the instance of the object itself
                                 #SELF represents the instance of the object itself or the class
        # Attributes
        # We take in the arguement
        # We assign it using self.attribute_name in this case self.breed
        self.breed = breed
        self.name = name

        
    # OPERATIONS/Actions ---> Methods
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))


# In[33]:


my_dog = Dog('Lab','Frankie')


# In[34]:


type(my_dog)


# In[35]:


my_dog.species


# In[36]:


my_dog.name


# In[43]:


my_dog.bark(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[62]:


class Circle():
    
    #CLASS OBJECT ATTRIBUTE
    pi = 3.14
     
    def __init__(self,radius=1): # <--- Can have a default value of 1 and then override below 
        
        self.radius = radius
        self.area = radius*radius*Circle.pi #<-- Can reference this in this manner because it is a class object attribute
        
    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2


# In[58]:


my_circle = Circle(30)  #<--- Overriding value of 30


# In[59]:


my_circle.pi


# In[60]:


my_circle.radius


# In[63]:


my_circle.area


# In[64]:


my_circle.get_circumference()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




