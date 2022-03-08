#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd 
import shutil
import time 


# In[2]:


def read_all_file (path) :
    output = os.listdir(path)
    file_list = []
    
    for i in output :
        if os.path.isdir(path +"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i) : 
            file_list.append(path+"/"+i)

    return file_list


# In[3]:


def copy_all_file(file_list, new_path) :
    for src_path in file_list:
         file = src_path.split("/")[-1]
         shutil.copyfile(src_path, new_path+"/"+file)


# In[4]:


src_path= "c:/Users/User/OneDrive/dataset/wow data/wowah/wow_2007/07_1"
new_path = "c:/Users/User/OneDrive/dataset/wow data/wow_07"
file_list = read_all_file(src_path)
copy_all_file(file_list, new_path)


# In[10]:


file_list = read_all_file(new_path)
os.listdir(new_path)


# In[11]:


folder = os.listdir(new_path)


# In[12]:


os.chdir(new_path)


# In[14]:


output= "c:/Users/User/OneDrive/dataset/wow data/wow_06/wow_06_complete.csv"
df_all = pd.DataFrame()
for file in folder :
     df = pd.read_csv(file, on_bad_lines='skip', sep=",",names=("d1","d2","d3","d4","d5", "d6","d7", "d8", "d9","d10", "d11"))
     df = pd.DataFrame(df)
     df_all = pd.concat([df_all, df],axis=0)


# In[17]:


df_all.head()


# In[21]:


df_all = df_all.drop([df_all.columns[0], df_all.columns[9], df_all.columns[10]], axis=1)


# In[22]:


df_all.head()


# In[27]:


df_all.dropna(subset=['d7'], inplace=True)


# In[28]:


df_all.to_csv(output)

