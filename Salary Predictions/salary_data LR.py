#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


salary_data = pd.read_csv(r"C:\Users\Aishwarya\Desktop\360DigitTMg\linear regression\Salary_Data.csv")
salary_data.head()


# In[3]:


salary_data.isnull().sum()


# In[4]:


salary_data.describe()


# In[5]:


salary_data.info()


# In[6]:


salary_data.iloc[np.where(salary_data["YearsExperience"] > 5.0)]["Salary"]


# In[7]:


salary_data.iloc[np.where(salary_data["Salary"] == max(salary_data["Salary"]))]


# In[8]:


x = salary_data.iloc[ : , [0]].values


# In[9]:


y= salary_data.iloc[ : , 1].values


# In[10]:


#splitting the dataset into train and test
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split( x , y , test_size = 0.2 , random_state = 42 )


# In[11]:


x_train.shape


# In[12]:


y_train.shape


# In[13]:


#Training of model on the dataset
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train , y_train)


# In[14]:


pred = model.predict(x_test)


# In[15]:


pred


# In[17]:


y_test


# In[22]:


#visualizing the training set result
import matplotlib.pyplot as plt
plt.figure(figsize = (5,5))
plt.scatter(x_train , y_train , color = "red")
plt.plot(x_train ,model.predict(x_train) , color = "blue")
plt.title("Salary vs Experience(Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[21]:


#visualizing the test set result
import matplotlib.pyplot as plt
plt.figure(figsize = (5,5))
plt.scatter(x_test , y_test , color = "red")
plt.plot(x_test , pred , color = "blue")
plt.title("Salary vs Experience(Testing set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[ ]:




