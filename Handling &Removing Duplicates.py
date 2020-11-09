#!/usr/bin/env python
# coding: utf-8

# # Handling and removing duplicates values

# In[1]:


# importing required packages
import pandas as pd


# In[3]:


# accessing dataset using pandas library
df=pd.read_csv("Dataset.csv")
df.head()#displaying first 5 row of dataset


# In[6]:


# Checking for duplicates values in whole dataset
sum(df.duplicated())# gives total number of duplicate values in dataset


# In[7]:


# Checking for duplicates values column wise
sum(df['Name'].duplicated())# gives total number of duplicate values in first column


# ## Removing duplicates

# In[10]:


# removing duplicate values using drop_duplicates()
df['Name'].drop_duplicates(inplace=True)# inplace is True for permenant change in dataset


# In[11]:


# Again Checking for duplicates values column wise
sum(df['Name'].duplicated())# gives total number of duplicate values in first column


# In[ ]:





# In[ ]:




