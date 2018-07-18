
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csv_path = "Resources/budget_data.csv"


# In[52]:


Budget_df = pd.read_csv(csv_path)
chrono_df = Budget_df.set_index("Revenue")

len(Budget_df)


# In[43]:


chrono_df.head()


# In[44]:



Budget_df[["Revenue"]].sum()
#print("Total Revenue: $" + Total_rev)


# In[45]:



Budget_df[["Revenue"]].mean()


# In[ ]:





# In[50]:


max_rev = Budget_df[["Revenue"]].max()
month_max = chrono_df.loc[max_rev, "Date"]
month_max


# In[51]:


min_rev = Budget_df[["Revenue"]].min()
month_min = chrono_df.loc[min_rev, "Date"]
month_min


# In[ ]:


print("Financial Analysis"
"----------------------------"
"Total Months: ")

