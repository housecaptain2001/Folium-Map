#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium


# In[2]:


world_map = folium.Map()


# In[3]:


world_map


# In[4]:


dehradun = folium.map.FeatureGroup()


# In[5]:


dehradun = dehradun.add_child(
    folium.CircleMarker(
    [30.3165, 78.0322], radius = 5,
    color = "red", fill_color="Red", fill = True, popup="Shridhar and Alex"
    )
)


# In[6]:


world_map.add_child(dehradun)


# In[7]:


kota = folium.map.FeatureGroup()


# In[8]:


kota = kota.add_child(
    folium.CircleMarker(
    [25.2138, 75.8648], radius = 5,
    color = "cyan", fill_color="cyan", fill = True, popup = "HARSH"
    )
)


# In[9]:


world_map.add_child(kota)


# In[10]:


Guwahati = folium.map.FeatureGroup()


# In[11]:


Guwahati = Guwahati.add_child(
    folium.CircleMarker(
    [26.1445, 91.7362], radius = 5,
    color = "green", fill_color="green", fill = True, popup = "Akshyata"
    )
)


# In[12]:


world_map.add_child(Guwahati)


# In[ ]:




