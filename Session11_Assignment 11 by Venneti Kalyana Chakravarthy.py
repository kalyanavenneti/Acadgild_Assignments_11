
# coding: utf-8
# It happens all the time: someone gives you data containing malformed strings, Python, lists and missing data. 

# How do you tidy it up so you can get on with the analysis?

#Take this monstrosity as the DataFrame to use in the following puzzles:

#df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
#'Budapest_PaRis', 'Brussels_londOn'],
#'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
#'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
#'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
#'12. Air France', '"Swiss Air"']})
# In[41]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[42]:


df


# In[43]:


# Question 1: Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row 
# so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column 
# (instead of a float column).

Flight_Number = []      ##List

for num in df['FlightNumber']:
    if np.isnan(num):
        num = prev_num+10
    prev_num = num
    Flight_Number.append(int(num))
    
df['FlightNumber']= Flight_Number
df


# In[36]:


# Question 2: The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ 
# to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.

df['From'] = [x.split('_', 1)[0] for x in df['From_To'].values]
df['To'] = [x.split('_', 1)[1] for x in df['From_To'].values]
df


# In[37]:


# Question 3: Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings
# so that only the first letter is uppercase (e.g."londON" should become "London".)

df['From'] = [x.title() for x in df['From'].values]
df['To'] = [x.title() for x in df['To'].values]
df


# In[38]:


# Question 4: Delete the From_To column from df and attach the temporary DataFrame from the previous questions.

df_temp=pd.DataFrame(df.drop(['From_To'], axis=1))
df_temp


# In[44]:


#Question 5a: In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each 
# first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, 
# the value should be NaN.

#Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and replace the unwanted 
#RecentDelays column in df with delays.

delays = df['RecentDelays'].apply(pd.Series)
delays = delays.rename(columns = lambda x : 'delay_' + str(x+1))
delays


# In[45]:


# Question 5b: Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and 
# Replace the unwanted RecentDelays column in df with delays.

#Replace the unwanted RecentDelays column in df with delays

df=df.drop('RecentDelays', axis=1).join(delays)
df

