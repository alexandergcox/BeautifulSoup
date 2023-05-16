#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## OpenWeather API: access and authorisation 

# This Notebook accompanies the **OpenWeather API: access and authorisation** activity. Follow the OpenWeather sign-up instructions and the introductory activity steps to learn how to:
# - get your OpenWeather API key
# - create a .env file
# - import the .env file into Jupyter Notebook
# - import the API key into Jupyter Notebook
# - connect with the OpenWeather API
# - retrieve weather data.

# **Important**
# 
# Please take note that you will work with the OpenWeather API. Keep in mind that the API is based on live and current weather data. Therefore, your output will differ from the outputs provided. 

# # 1. OpenWeather API key

# Get your API key from this website: https://openweathermap.org/api
# 
# Ensure:
# - your account is activated
# - you have copied your key.
# 

# # 2. Create a .env file

# You will need your API key. Follow the steps described in **5.2.5 API access and authorisation** to create your file and store your key securely. Make sure that your .env file is in the same directory as the Notebook you are working in.![env%20txt.jpg](attachment:env%20txt.jpg)

# # 3. Import libraries

# In[3]:


#Uncomment if you need to install dotenv.
#!pip install python-dotenv

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 


# # 4. Access your OpenWeather API key

# In[5]:


# Locate and read the key from your .env file.
API_key = os.getenv('4199530758f704f528876e613f7402f4')

# It is not good practice to print or share your API key, but you are printing it just this once as a test.
print(API_key)


# # 5. Connecting to OpenWeather

# In[6]:


# Create an API call, excluding some fields to reduce the output.
weather_url = "https://api.openweathermap.org/data/3.0/onecall?lat=51.509865&lon=-0.118092&exclude=minutely,hourly,daily" "&appid=" + 4199530758f704f528876e613f7402f4


# In[7]:


# Define a response variable.
resp = requests.get(weather_url)


# In[ ]:


# Print the response.
print("Today's weather:" , resp.json())

