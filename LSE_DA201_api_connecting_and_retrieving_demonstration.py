#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## API: Connecting and retrieving (tutorial video)

# This Notebook accompanies the **API: Connecting and retrieving** demonstration video. Follow along with the demonstration to learn how to:
# - request access
# - retrieve headers
# - retrieve header values
# - formating the JSON response.

# # Prepare your workstation

# In[1]:


# Install JSON and requests if needed.
# !pip install json
# !pip install requests


# In[2]:


# Import libraries.
import requests
import json


# # 1. Request access

# In[3]:


# Identify the URL to connect to.
# Create a variable to store the URL.
URL = 'https://api.coingecko.com/api/v3/exchange_rates'

# Send connect request.
response = requests.get(url=URL)

# View answer from URL.
print(response)


# # 2. Retrieve headers

# What if you do not get a `200 status_code`? Can you still access some information from the API? Yes, you can!

# In[4]:


# Write if and else statements to get information and status_code.
if response.status_code == 200:
    print(response.headers)
else:
    print(response.status_code)
    response.headers['Content-Encoding']


# # 3. Retrieve header values

# In[5]:


# Retrieving header values with a key.
print(response.headers['Date'])


# In[6]:


# Retrieving header values with a key.
print(response.headers['Access-Control-Allow-Methods'])


# # 4. Retrieve information from API

# In[7]:


# Retrieve the payload of the API.
response.text


# In[8]:


# Type of content.
print(type(response))


# # 5. Format JSON text

# In[9]:


# Change response to json.
response.json()


# In[10]:


# Get the information again from the API.
r = requests.get(url=URL)

# View the information.
print(type(r.text))
print(r.text)


# In[11]:


# Parse JSON data with loads().
content = json.loads(r.text)

# View the content.
print(type(content))
print(content['rates'])


# In[12]:


# Formatting JSON.
print(json.dumps(content, indent=4))


# In[13]:


# Formatting JSON.
print(json.dumps(content, indent=4, separators=('. ', ' = ')))


# In[ ]:




