#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(n1,n2):
    print(n1+n2)


# In[2]:


add(10,20)


# In[3]:


number1 = 10


# In[4]:


number2 = input("Please provide a number: ")


# In[17]:


add(number1,number2)
print("Something happened!")


# In[24]:


try: 
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
except: 
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)


# In[21]:


result


# In[ ]:





# In[ ]:


try:
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print('All other exceptions')
finally:
    print("I always run")


# In[ ]:


def ask_for_int():
    
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! that is not a number")
            continue
        else:
            print("Yes thank you!")
            break
        finally:
            print("Yes thank you!")
            


# In[ ]:


ask_for_int()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




