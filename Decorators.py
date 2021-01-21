#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    return 1


# In[2]:


func()


# In[3]:


func


# In[4]:


def hello():
    return "Hello!"


# In[5]:


hello()


# In[6]:


hello


# In[7]:


greet = hello


# In[8]:


greet()


# In[9]:


del hello


# In[10]:


hello()


# In[11]:


greet()


# In[32]:


def hello(name='Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
    
    print("I am going to return a function!!")
    
    if name == 'Jose':
        return greet
    else:
        return welcome


# In[33]:


my_new_func = hello('jose')


# In[35]:


my_new_func()


# In[36]:


def cool():
    
    def super_cool():
        return('I am very cool')
    
    return super_cool


# In[37]:


some_func = cool()


# In[40]:


some_func()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[42]:


def hello():
    return "Hi Jose!"


# In[43]:


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


# In[44]:


other(hello) 


# In[ ]:





# In[56]:


def new_decorator(original_func):
    
    def wrap_func():
        
        print('Some extra code, before the original function')
        
        original_func()
        
        print('Some extra code, after the original function')
        
    return wrap_func


# In[57]:


def func_needs_decorator():
    print("I want to be decorated!!")


# In[58]:


func_needs_decorator()


# In[59]:


decorated_func = new_decorator(func_needs_decorator)


# In[60]:


decorated_func()


# In[61]:


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")


# In[62]:


func_needs_decorator()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




