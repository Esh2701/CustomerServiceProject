#!/usr/bin/env python
# coding: utf-8

# In[26]:


#loaded the data set of the customer service
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('311_Service_Requests_from_2010_to_Present.csv')
df.head()


# In[27]:


#identified the shape of the data set
df.shape


# In[28]:


#identified the variable with null values
df.isna().sum()


# In[29]:


#utilize the missing value treatment
df.isnull().sum()


# In[30]:


df.tail(5)


# In[31]:


df.head(5)


# In[32]:


df.info()


# In[34]:


df.describe()


# In[36]:


# perform data exploratory analysis
df.columns= df.columns.str.replace(" ", "_")


# In[3]:


sns.set()
dataframe.isnull().sum().plot(kind='barh', alpha= 0.7, figsize= (18,15), title="Column-wise NULL Value Count")
plt.xlabel('NULL Value Count')
plt.ylabel('Column Name')
plt.show()


# In[38]:


#Analyze the date column and remove the entries if it has incorrect timeline
df[['Closed_Date', 'Created_Date']].isnull().sum()


# In[50]:


# Frequency Plot for complaints in each city
sns.set()
df['City'].value_counts().sort_values(ascending= True).plot(kind= 'barh', figsize=(17,15), title="City-wise Complaint Count")
plt.xlabel('Complaint Count')
plt.ylabel('City')
plt.show()


# In[51]:


brooklyn_data = df[df['City']=='BROOKLYN']
brooklyn_data[['Longitude', 'Latitude']].plot(kind='scatter', 
                                         x='Longitude', 
                                         y='Latitude', 
                                         figsize=(10,8), 
                                         title = 'Complaints Concentration Across Brooklyn'
                                        ).axis('equal')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# In[52]:


# Hexbin plot to visualize the complaint concentration 
brooklyn_data.plot(kind='hexbin', 
              x='Longitude', 
              y='Latitude', 
              gridsize=40,
              colormap = 'jet',
              mincnt=1,
              title = 'Complaints concentration across Brooklyn',
              figsize=(10,6)
             ).axis('equal')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# In[53]:


# Find the major type of complaints

# PLot a bar graph of types of complaints vs graph count
sns.set()
df['Complaint_Type'].value_counts().plot(kind= 'bar', figsize=(17,12), title="Count of each type of complaint")
plt.xlabel('Complaint Type')
plt.ylabel('Complaint Count')
plt.show()
df['City'].unique()


# In[57]:


# frequency of various type of complaints in New York City
df.loc[df['City']== 'NEW YORK']['Complaint_Type'].value_counts()


# In[60]:


# find the 10 types of complaints
df['Complaint_Type'].value_counts()[0:10]


# In[64]:


#Display the types of complaints in each city in a separate dataset
df_new= pd.DataFrame()
for i in df['City'].unique():
    df_new[i]= df.loc[df['City']== i]['Complaint_Type'].value_counts()
df_new.head()


# In[ ]:


# Visualize the major types of complaints in each city


# In[65]:


sns.set()
df_new.T.plot(kind= 'barh', stacked= True, figsize= (19, 35), title="City-wise Complaint Count")
plt.xlabel('Complaint Count')
plt.ylabel('City')
plt.show()


# In[66]:


df_new_T= df_new.T
sns.set()
f, ax = plt.subplots(figsize=(20, 30))
sns.heatmap(df_new_T[top10_complaints], annot=True, cbar=False, linewidths=.8, ax=ax)
plt.show()


# In[72]:


# identifying the significant variables by performing a statistical analysis using chi-square values
contingency_table = pd.crosstab(df['City'],df['Complaint_Type'], margins= True)


# In[73]:


contingency_table.shape


# In[74]:


contingency_table.iloc[0:5][0:24].values


# In[75]:


f_obs= []
for i in range(0, contingency_table.shape[0]-1):
    f_obs.append(contingency_table.iloc[i][0:24].values)
f_obs= np.array(f_obs)
f_obs[0:5]


# In[76]:


from scipy import stats
stats.chi2_contingency(f_obs)[0:3]


# In[ ]:





# In[ ]:




