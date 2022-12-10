#!/usr/bin/env python
# coding: utf-8

# In[8]:


#import data


# In[9]:


get_ipython().system('pip install kaggle')


# In[10]:


#!mkdir ~/.kaggle


# In[11]:


get_ipython().system('cp /Users/zhenglanhuang/Downloads/kaggle.json /Users/zhenglanhuang/.kaggle/kaggle.json')


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


# In[ ]:


get_ipython().system('chmod 600 /Users/zhenglanhuang/.kaggle/kaggle.json')


# In[ ]:


api.dataset_download_file('annavictoria/speed-dating-experiment', 'Speed Dating Data.csv')


# In[ ]:


data = pd.read_csv('Speed%20Dating%20Data.csv.zip', encoding=('ISO-8859-1'))
    


# In[ ]:


data


# In[ ]:


#clean data: What do you look for in the opposite sex?


# In[ ]:


look4 = data[['gender','attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1']]
look4['gender'] = look4['gender'].replace([0,1],['Women','Men'])
final_look4 = look4.groupby('gender').mean()
final_look4


# In[ ]:


#plot: What do you look for in the opposite sex?


# In[ ]:


men.look4 = list(final_look4.iloc[0])
women.look4 = list(final_look4.iloc[1])


# In[ ]:


x = ['Attractive','Sincere','Intelligent','Fun','Ambitious','Shared Interests']
x_axis = np.arange(len(x))
plt.subplots(figsize=(10,5))
plt.bar(x_axis - 0.2, men, 0.4, label = 'Men', color = '#d4e69c')
plt.bar(x_axis + 0.2, women, 0.4, label = 'Women', color = '#ffe1df')
plt.title('What People Are Looking For in the Opposite Sex?')
plt.xticks(x_axis, x)
plt.legend()
plt.show()


# In[ ]:


#clean data: What do you think the opposite sex looks for in a date? 


# In[ ]:


oplook = data[['gender','attr2_1','sinc2_1','intel2_1','fun2_1','amb2_1','shar2_1']]
oplook['gender'] = oplook['gender'].replace([0,1],['Women','Men'])
final_oplook = oplook.groupby('gender').mean()
final_oplook


# In[ ]:


#plot: What do you think the opposite sex looks for in a date? 


# In[ ]:


men_oplook = list(final_oplook.iloc[0])
women_oplook = list(final_oplook.iloc[1])


# In[ ]:


plt.subplots(figsize=(10,5))
plt.bar(x_axis - 0.2, men_oplook, 0.4, label = 'Men', color = '#ffe1df')
plt.bar(x_axis + 0.2, women_oplook, 0.4, label = 'Women', color = '#d4e69c')
plt.title('What do you think the opposite sex looks for in a date? ')
plt.xticks(x_axis, x)
plt.legend()
plt.show()


# In[ ]:


#clean data: First vs last speed date on chance of getting a second date(match vs variables)


# In[ ]:




