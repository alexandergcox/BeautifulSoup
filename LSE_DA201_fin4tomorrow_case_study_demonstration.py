#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Fin4Tomorrow case study (demonstration)

# James Roberts is a data analyst at Fin4Tomorrow, an organisation that provides financial advice to businesses. Fin4Tomorrow is compiling a quarterly report on how businesses are performing to identify promising investment opportunities for their clients. James was tasked to provide a list of the world's largest companies by revenue. As James is fairly new to web scraping with Python, he decides to play around and perform web scraping of a Wikipedia website - [List of largest companies by revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue) (Wikipedia 2021). 
# 
# See if you can follow along with James and get the same outputs.

# # 1. Establish connection with the website

# In[2]:


# Import libraries requests
import requests
from bs4 import BeautifulSoup


# In[3]:


# Create a variable to save the URL.
url = 'http://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

# Specify the URL and request with get().
r = requests.get(url)

# Determine a connection.
if r.status_code ==200:
    html_doc = r.text
    
# View data.
print(r)


# # 2. Extract data from the website

# In[4]:


# Set BeautifulSoup object.
soup = BeautifulSoup(html_doc)

# Print output.
print(soup.prettify())


# In[ ]:





# # 3. Extract data from the table

# In[5]:


# Find the table elements.
tables = soup.find_all('table')

# Show all the tables.
tables


# In[ ]:





# # 4. Set the target table

# In[6]:


# The table we want is the first one.
list_of_companies = tables[0]


# In[7]:


# Print the output.
list_of_companies


# # 5. Extract all the rows

# In[8]:


# Show all of the rows of the table.
rows = list_of_companies.find_all('tr')

# Storage for the extracted data.
output = []

# Specify column names.
column_names = ['Name', 'Industry', 'Revenue', 'Profit', 'Employees', 'Headquarters', 'Ref']

# Create a for loop statement.
for company in rows:
    company_data = company.find_all('td')
    if company_data:
        # extract the text within each element
        company_text = [td.text for td in company_data]
        output.append(dict(zip(column_names, company_text)))
        
# View the output.
output


# In[ ]:





# # 6. Create a Pandas DataFrame

# In[9]:


# Import Pandas.
import pandas as pd

# Create a DataFrame.
data=pd.DataFrame(output)

# Subset data with only relevant columns.
data_companies = data[['Name', 'Revenue', 'Headquarters']]

# View the DataFrame
data_companies


# In[10]:


# web scraping for multiple sources
# Specify the URLs

urls = ['https://en.wikipedia.org/wiki/Walmart',
       'https://en.wikipedia.org/wiki/State_Grid_Corporation_of_China']

# Write a for loop statement.
for url in urls:
    r = requests.get(url)
    if r.status_code == 200:
        html_doc = r.text
        
        # Create BeautifulSoup object.
        soup = BeautifulSoup(html_doc)
        
for image_url in soup.find_all('img'):
    lower_case_text = str(image_url).lower()
    if 'logo' in lower_case_text:
        print("https:" + image_url['src'])


# # 7. Extract Pandas DataFrame: JSON and CSV

# In[11]:


# import JSON library.
import json

# Export the output as a JSON file.
output_json = json.dumps(output)

# View the output.
print(output_json)


# In[13]:


# Read JSON using Pandas, output to .csv.
pd.read_json(output_json).to_csv('list_of_companies.csv', index=False)

# Save the JSON file to .json.
with open('list_of_companies.json', 'w') as f:
    json.dump(output, f)


# # 8. Import CSV and JSON files

# In[14]:


# Import and read the CSV file.
data_csv = pd.read_csv('list_of_companies.csv')

# View the DataFrame.
print(data_csv.head())


# In[16]:


# Import and read the JSON file.
data_json = pd.read_json('list_of_companies.json')

# View the data.
data_json.head()


# In[ ]:




