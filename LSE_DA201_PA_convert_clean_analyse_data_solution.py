#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Convert, clean, and analyse data

# **This is the solution to the activity.**
# 
# Having scraped and shared the specific data required by the executives, claims department, and clients of your organisation, you now need to share it with them. You know that none of the stakeholders involved are as tech- or data-savvy as you are, and that you need to share the data with them in a way they can understand and use. To this end, you’ve been asked to download your scraped data as a CSV file. 
# 
# Additionally, other data analysts at your organisation want access to your data, and have requested the data also be shared as JSON files. Your analytics department has also asked you to focus on the six continents on the table, and perform several calculations for each of them.

# ## 1. Import the libraries

# In[1]:


# Import necessary libraries.
import requests
import pandas as pd
from bs4 import BeautifulSoup


# ## 2. Establish connection with URL

# In[2]:


# Create a URL variable.
url = 'https://www.worldometers.info/coronavirus/'

# Create a requests variable.
r = requests.get(url)

# Make contact with the website.
if r.status_code == 200:
    html_doc = r.text
    
# Create a BeautifulSoup object.
soup = BeautifulSoup(html_doc)

# View the output.
print(soup.prettify())


# ## 3. Extract tabular data

# In[3]:


# Extracting the contents of the table with the table id: 
table = soup.find('table', attrs={'id': 'main_table_countries_today'})

# View the output.
table


# ## 4. Extract table headers

# In[4]:


# Now we need to specify BeautifulSoup to go through the table and find everything 
# with a tr tag.
# Note: th = (table header), tr = (table row), and td = table column.
rows = table.find_all('tr', attrs={'style': ""})

# View the output.
rows


# In[5]:


# Storage for the extracted data.
# Create an empty list.
output = []

# Specify the column names.
column_names = ['Country,Other', 'Total Cases', 'New Cases', 'Total Deaths',
               'New Deaths', 'Total Recovered', 'New Recovered',
               'Active Cases', 'Serious, Critical', 'Tot Cases/ 1M pop',
               'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population']

# Create a for loop statement.
for cases in rows:
    cases_data = cases.find_all('td')
    if cases_data:
        # Extract the text within each element.
        cases_text = [td.text for td in cases_data]
        output.append(dict(zip(column_names, cases_text)))
        
# View the output.
output


# ## 5. Convert extracted data into a Panda DataFrame

# In[6]:


# Create a DataFrame directly from the output.
data = pd.DataFrame(output)

# View the DataFrame.
data.head()


# ## 6. Convert, clean and analyse the data

# In[7]:


# Save the DataFrame as a CSV file without index.
data.to_csv('cases.csv', index=False)


# In[8]:


# Create a JSON file.
import json

# Create a JSON file.
output_json = json.dumps(output)

# View the output.
output_json


# In[9]:


# Save the JSON file to .json.
with open('cases_json.json', 'w') as f:
    json.dump(output, f)


# In[10]:


# Read the JSON using Pandas, output to .csv.
pd.read_json(output_json).to_csv('cases_csv.csv', index=False)


# In[11]:


# Import and read the CSV file.
data_csv = pd.read_csv('cases_csv.csv')

# View the data.
print(data_csv.head())

# Import and read the JSON file.
data_json = pd.read_json('cases_json.json')

# View the DataFrame. 
data_json.head()


# In[12]:


# View the CSV and JSON DataFrames.
print(data_csv.dtypes)
print(data_csv.columns)

print(data_json.dtypes)
print(data_json.columns)


# In[13]:


# Create a subset.
data_report = data_csv[['Country,Other', 'Total Cases', 'Total Deaths',
                        'Total Recovered', 'Active Cases', 'Serious, Critical']]

# View the column names.
print(data_report.columns)
data_report


# In[14]:


# Determine missing values.
data_report.isnull().sum()


# In[15]:


# Save the DataFrame as a CSV file without index.
data_report.to_csv('cases_report.csv', index=False)


# In[16]:


# View the saved CSV.
cases_report = pd.read_csv('cases_report.csv')

# View the DataFrame.
cases_report.head()


# In[ ]:




