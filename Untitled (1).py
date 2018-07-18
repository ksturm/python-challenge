
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


csv_path = "Resources/election_data.csv"


# In[4]:


election_df = pd.read_csv(csv_path)
election_df.head()


# In[5]:


len(election_df)


# In[6]:


election_df.Candidate.unique()


# In[8]:


election_df.count()


# In[10]:


candidate_counts = election_df["Candidate"].value_counts()
candidate_counts


# In[11]:


E = election_df.groupby("Candidate").count()
E

