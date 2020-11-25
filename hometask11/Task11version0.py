#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Задание 1. 


# In[3]:


import pandas as pd


# In[5]:


visits = pd.read_csv('visit_log.csv', sep=';')
visits.head()


# In[31]:


visits.loc[(visits.traffic_source == 'yandex') | (visits.traffic_source == 'google'), 'source_type'] = 'organic'
visits.loc[(visits.traffic_source == 'mail') | (visits.traffic_source == 'paid') & (visits.region == 'Russia'), 'source_type'] = 'ad'
visits.loc[(visits.traffic_source == 'mail') | (visits.traffic_source == 'paid') & (visits.region != 'Russia'), 'source_type'] = 'other'
visits.loc[visits.traffic_source == 'direct', 'source_type'] = visits.traffic_source
visits


# In[ ]:


# Задание 2.


# In[35]:


url = pd.read_csv('URLs.txt ', sep=';')
url


# In[39]:


news = url[url.url.str.contains('/\d{8}-')]
news


# In[ ]:


# Задание 3. 


# In[42]:


from pymystem3 import Mystem

data = pd.DataFrame({
    'keyword': ['курс гривны к рублю', 'доллары в рубли', '100 долларов в рублях', 'курс рубля'],
    'shows': [125076, 114173, 97534, 53546],
})
data


# In[43]:


m = Mystem()
lemmas = m.lemmatize(data)
data['lemmas'] = str(lemmas)

data


# In[ ]:




