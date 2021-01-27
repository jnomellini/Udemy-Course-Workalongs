#!/usr/bin/env python
# coding: utf-8

# In[4]:


import datetime


# In[20]:


mytime = datetime.time(13,20,1,20)


# In[21]:


mytime.minute


# In[22]:


mytime.hour


# In[23]:


print(mytime)


# In[24]:


mytime.microsecond


# In[25]:


type(mytime)


# In[26]:


today = datetime.date.today()


# In[27]:


print(today)


# In[28]:


today.month


# In[29]:


today.year


# In[30]:


today.ctime()


# In[31]:


from datetime import datetime


# In[33]:


mydatetime = datetime(2021,10,3,14,20,1)


# In[35]:


print(mydatetime)


# In[37]:


mydatetime = mydatetime.replace(year=2020)


# In[38]:


print(mydatetime)


# In[ ]:


# DATE INFORMATION


# In[39]:


from datetime import date


# In[40]:


date1 = date(2021,11,3)
date2 = date(2020,11,3)


# In[42]:


result = date1 - date2


# In[43]:


type(result)


# In[44]:


result.days


# In[45]:


datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)


# In[46]:


datetime1 - datetime2


# In[47]:


36000/60/60


# In[48]:


mydiff = datetime1 - datetime2


# In[49]:


mydiff.seconds


# In[50]:


mydiff.total_seconds()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




