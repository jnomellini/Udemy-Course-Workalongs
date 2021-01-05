#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming
# ## Homework Assignment
# 
# #### Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

# In[12]:


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor1
        
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)


# In[13]:


coordinate1 = (3,2)  
coordinate2 = (8,10) 

li = Line(coordinate1,coordinate2)


# In[14]:


li.distance()


# In[15]:


li.slope()


# ________
# #### Problem 2

# Fill in the class 

# In[10]:


class Cylinder():
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)
    


# In[11]:


# EXAMPLE OUTPUT
c = Cylinder(2,3)


# In[12]:


c.volume()


# In[13]:


c.surface_area()

