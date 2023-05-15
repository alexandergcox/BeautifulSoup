#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Scraping COVID data

# **This is the solution to the activity.**
# 
# You work as a data analyst at a health insurance company. To provide up-to-date information for the executive, claims department, and clients, you are tasked with gathering the latest data on worldwide COVID-19 cases. 
# 
# Each department requires different information. For each continent on the list:
# The executive needs to know:
# - Total cases
# - Total deaths
# 
# Claims needs to know:
# - New cases
# - New deaths
# - Active cases
# - Serious, Critical
# 
# Clients need to know:
# - Total cases
# - Total recovered
# - Newly recovered

# ## 1. Import the libraries

# In[1]:


# Import the necessary packages.
import requests
import pandas as pd
from bs4 import BeautifulSoup


# ## 2. Establish connection with URL

# In[2]:


# Create a url variable.
url = 'https://www.worldometers.info/coronavirus/'

# Create a requests variable.
r = requests.get(url)

# Make contact with the website.
if r.status_code == 200:
    html_doc = r.text
    
# Get a BeautifulSoup object.
soup = BeautifulSoup(html_doc)

# Print the output.
print(soup.prettify())


# ## 3. Extract tabular data

# In[3]:


# Extract the contents of the table with the table id. 
table = soup.find('table', attrs={'id': 'main_table_countries_today'})

# View the table.
table


# ## 4. Extract table headers

# In[4]:


# Specify BeautifulSoup to go through the table and find everything 
# with a tr tag.
# Note: th = (table header), tr = (table row), and td = table column
rows = table.find_all('tr', attrs={'style': ""})

# View the result.
rows


# In[5]:


# Store the extracted data.
output = []

column_names = ['Country,Other', 'Total Cases', 'New Cases', 'Total Deaths',
               'New Deaths', 'Total Recovered', 'New Recovered',
               'Active Cases', 'Serious, Critical', 'Tot Cases/ 1M pop',
               'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population']

# Create a for loop statement.
for cases in rows:
    cases_data = cases.find_all("td")
    if cases_data:
        # Extract the text within each element.
        cases_text = [td.text for td in cases_data]
        output.append(dict(zip(column_names, cases_text)))
        
# Create an output.
output


# ## 5. Convert extracted data into a Panda DataFrame

# In[6]:


# Create a DataFrame directly from the output.
data = pd.DataFrame(output)

# View the DataFrame.
data.head()


# In[ ]:




