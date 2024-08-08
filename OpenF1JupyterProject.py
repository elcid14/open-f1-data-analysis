#!/usr/bin/env python
# coding: utf-8

# In[8]:


from urllib.request import urlopen
from io import StringIO
import json
import numpy as np
import pandas as pd
import aiohttp

# Get the drivers to start formatting data properly for later transformations
response = urlopen('https://api.openf1.org/v1/drivers?meeting_key=latest')
data = json.loads(response.read())


driverDf = pd.DataFrame(data)
print(driverDf)


# In[11]:


# So we created the data frame succesfully but there is an issue
# The data is not readable, there is duplicate keys for meeting_id and session_key
# Drop the duplicate data, and add the necessary columns we need such as first_name, last_name, etc. 

driverDf_deduped = driverDf.drop_duplicates(subset='driver_number')

req_columns = ['driver_number','full_name', 'team_name', 'name_acronym']

driverDf = driverDf_deduped[req_columns]

print(driverDf)


# In[14]:


# Now that we ahve our driver df we can start to make data insisghts with different api calls.
# The first insight we want to gather is the number of laps where the driver was recorded over 300 kmh
# This is looking at the course speed trap, which is generally the fastest section of a track, not the average speed of a lap
# For this we will combine two data frames. The first one we created and a new one that will have the driver number and various speed columns
# After processing the second data frame we will combine the two where only the speed is above 300 kmh and if a driver has not reached that speed we will default to 0


# The df before merging will look like ["row", "driver_number", "number_laps_greater_than_300",]
# We will then merge the two on driver_number in the first df, adding the additonal column number_laps_greater_than_300


# Cince there is so much lap data per driver per season we need to make an async task to iterate through each param value
# We need to gather each session_key and each driver number, and create a params_list that has a tuple of each
# Example params_list = set(('driver_numner':'1','session_key':'1'),('driver_numner':'2','session_key':'2') )
# we will use asyncio and aiohttp to gather all the data, then store it in json and create the dataframe



# now that we have 


# In[ ]:




