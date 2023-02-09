#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install phonenumbers


# In[11]:


import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = "+9188XXXXXXXX"
number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))


# In[ ]:




