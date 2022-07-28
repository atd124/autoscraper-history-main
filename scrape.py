#!/usr/bin/env python
# coding: utf-8

# In[38]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[23]:


response = requests.get("https://www.mlb.com/mets")
doc = BeautifulSoup(response.text, 'html.parser')


# In[82]:


titles = doc.select('.p-featured-content__body a')
titles


# In[ ]:





# In[83]:


rows = []

for title in titles:
    row = {}
    
    row['title'] = title.text.strip()
    row['url'] = title['href']
    
    rows.append(row)
    
rows

df = pd.DataFrame(rows)
df.head(10)


# In[106]:


mets = doc.select('.p-featured-content__body')

rows = []

for met in mets:
    
    row = {}
    
    row['headline'] = (met.select_one('.u-text-flow').text.strip())
    row['url'] = (met.select_one('a')['href'])
    
    print(row)
    rows.append(row)


# In[107]:


import pandas as pd

df = pd.DataFrame(rows)
df


# In[108]:


df.to_csv("mets-headlines.csv", index=False)


# In[ ]:




