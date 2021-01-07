#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming Challenge
# 
# For this challenge, create a bank account class that has two attributes:
# 
# * owner
# * balance
# 
# and two methods:
# 
# * deposit
# * withdraw
# 
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# In[37]:


class Account:
    
    def __init__(self,owner,balance=0):
        self.owner = owner        
        self.balance = balance
           
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount Balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit accepeted!')
           
    def withdraw(self,wth_amt):
        if self.balance >= wth_amt:
            self.balance -= wth_amt
            print('Withdrawal accepted!')
        else:
            print('Funds Unavailable!')


# In[40]:


# 1. Instantiate the class
acct1 = Account('Jose',100)


# In[41]:


# 2. Print the object
print(acct1)


# In[42]:


# 3. Show the account owner attribute
acct1.owner


# In[43]:


# 4. Show the account balance attribute
acct1.balance


# In[44]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


# In[45]:


acct1.withdraw(75)


# In[46]:


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# ## Good job!
