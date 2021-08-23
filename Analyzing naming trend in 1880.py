#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# we have a data of baby names in 1880(year),we have to analyze the most popular baby name


# In[48]:


babynm=pd.read_csv("D:\\yob1880.txt",names=["Name","Gender","Times"])


# In[49]:


babynm


# In[ ]:


#to find the number of male and female


# In[50]:


pd.value_counts(babynm["Gender"])


# In[18]:


babynm["Name"].nunique()


# In[19]:


babynm=babynm.drop_duplicates("Name",keep="last")


# In[20]:


#to plot no of male and female baby


# In[21]:


babynm=babynm.sort_values(["Name"])


# In[22]:


babynm


# In[23]:


babynm=babynm[["Gender"]]


# In[24]:


babynm


# In[34]:


#data visualitaion for gender column


# In[53]:


babynm["Gender"].value_counts().keys().tolist()


# In[54]:


babynm["Gender"].value_counts().tolist()


# In[60]:


plt.bar(babynm["Gender"].value_counts().keys().tolist(),babynm["Gender"].value_counts().tolist(),color="red")
plt.ylabel("no of babies")
plt.xlabel("count")
plt.title("visualising the Gender")


# In[65]:


# ordering the times by maxm no


# In[62]:


babynm.sort_values("Times",ascending=False)


# In[67]:


babynm.sort_values("Times",ascending=False).head(100)


# In[68]:


print("popular baby names=",babynm.sort_values("Times",ascending=False).head(100))


# In[69]:


# Here we can find that John is the most popular baby name in 1880 ,whic has 9655 times .


# In[ ]:





# In[ ]:




