#!/usr/bin/env python
# coding: utf-8

# In[14]:


#pip install pandas
import pandas as pd
from pandas import DataFrame 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm 
df = pd.read_csv("C:\\Users\\User\\Downloads\\lmdata.csv")
print(df)


# In[19]:


df.shape


# In[20]:


df.columns


# In[11]:


df.head


# In[21]:


df.head(5)


# In[22]:


df.describe()


# In[23]:


df.describe().T


# In[24]:


x = df['latitude'] 
y = df['mortality']


# In[28]:


plt.title('Latitude vs Mortality Relationship')
plt.xlabel('Latitude')
plt.ylabel('Mortality')
plt.gcf().autofmt_xdate()
    
plt.plot(x,y)
plt.show()


# In[30]:


plt.title('Latitude vs Mortality Relationship')
plt.xlabel('Latitude')
plt.ylabel('Mortality')
plt.gcf().autofmt_xdate()

df.plot(kind='scatter',x='latitude',y='mortality')


# In[3]:


results = sns.boxplot(x=df['mortality'])
results.set(title='Mortality Rate',xlabel='Latitude',ylabel='Mortality')
plt.show()


# In[4]:


#Conduct a Pearson's correlation test for Test for the variables
df.corr()


# In[5]:


#7: Create a pair plot for the data
sns.pairplot(df)


# In[6]:


#Description
df.describe().T


# In[8]:


#Create a seaborn regplot of the regression model and the 95% confidence Interval
nancy = sns.regplot(df.latitude,df.mortality)
nancy.set(title="Linear regression Model")
plt.show()


# In[11]:


#Ordinary Least Squares in Python | DataRobothttps://www.datarobot.com › Blog › AI & ML Expertise
#Feb. 8, 2014 — Linear regression, also called Ordinary Least-Squares (OLS) Regression, 
#is probably the most commonly used technique in Statistical Learning. It is also the oldest, 
#dating back to the eighteenth century and the work of Carl Friedrich Gauss and Adrien-Marie Legendre

#Create a regression model using old() from the statsmodel package
njoki = df.latitude
njoki1 = df.mortality
model = ols("latitude ~ mortality", df)
results = model.fit()
print(results.summary())


# In[12]:


#calculate the residual for the regression test
residuals = results.resid
predicted = results.fittedvalues
sns.regplot(x=residuals, y=predicted)


# In[16]:


#Mean of the residuals
print('################# Mean of Residuals = #################', np.mean(residuals)) #mean of residuals = 0


# In[ ]:




