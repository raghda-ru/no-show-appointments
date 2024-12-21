#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [No-Show-Appointments]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > **Tip**: In this section of the report, provide a brief introduction to the dataset you've selected/downloaded for analysis. Read through the description available on the `Project Details` page of `Investigate a Dataset` lesson for this course. List all column names in each table, and their significance. In case of multiple tables, describe the relationship between tables. 
# 
# 
# ### Question(s) for Analysis
# >**Tip**: Clearly state one or more questions that you plan on exploring over the course of the report. You will address these questions in the **data analysis** and **conclusion** sections. Try to build your report around the analysis of at least one dependent variable and three independent variables. If you're not sure what questions to ask, then make sure you familiarize yourself with the dataset, its variables and the dataset context for ideas of what to explore.
# 
# > **Tip**: Once you start coding, use NumPy arrays, Pandas Series, and DataFrames where appropriate rather than Python lists and dictionaries. Also, **use good coding practices**, such as, define and use functions to avoid repetitive code. Use appropriate comments within the code cells, explanation in the mark-down cells, and meaningful variable names. 

# In[1]:


# import statements for all of the packages.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint

get_ipython().run_line_magic('matplotlib', 'inline')



# <a id='wrangling'></a>
# ## Data Wrangling
# 

# In[2]:


# load data and check how much row and columns it contains.
df = pd.read_csv('Database_No_show_appointments/noshowappointments-kagglev2-may-2016.csv')
df.shape


# In[3]:


# show data
df.head(3)


# In[4]:


# In the below cells we will see the data information
df.info()


# ##### There's no NaN values in any of the columns.

# In[5]:


#checking if there's any duplicates
sum(df.duplicated())


# In[6]:


sum(df["AppointmentID"].duplicated())


# ##### There is no duplicate rows or appointment IDs.

# In[7]:


# illustrate data
df.describe()


# ##### it appears that the 'age' column has a negative value that should be cleaned.

# # Data Cleaning

# #### By checking it appears that we have PatientID as float and gonna convert to integer, also both of the ScheduledDay and AppointmentDay have false types and it will be converted to datetime

# In[8]:


df['PatientId'] = df['PatientId'].astype('int')
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])


# In[9]:


# Make the column names lower-case and uniform
df.columns = df.columns.str.lower().str.replace('-', '_')
#df.columns


# In[10]:


# To clean "Age" column, first let's see how many rows have this problem.
print(df[df['age'] == -1])
df.drop(index=df[df['age']==-1].index, inplace=True)


# In[11]:


df['no_show'].value_counts()


# # Exploratory Data Analysis

# ## How many people make an appointment and did not show up?

# In[12]:


fig, ax = plt.subplots(figsize=(5,5))
df['no_show'].value_counts(normalize=True).plot.pie(ax=ax, labels=["showed up", "Didn't show up"], autopct='%1.1f%%')
ax.set_title('The percentage of patients that showed up and did not showed up for the appointment.')


# In[13]:


print(df['no_show'].value_counts())


# ### As seen above around 20.19 percent of the people doesn't show up

# In[14]:


ax = sns.countplot(x=df['gender'], hue=df['no_show'], data=df)
ax.set_title("Show/NoShow for Females and Males")
x_ticks_labels=['Female', 'Male']
ax.set_xticklabels(x_ticks_labels)
plt.show()


# ### It indicates that the number of the Women who showed up is greater than the Men's number 

# In[15]:


## choose the important features and droping unnecessary columns
df.drop(columns='appointmentid', inplace=True)


# ## What factors are important for us to know in order to predict if a patient will show up for their scheduled appointment?

# ###  1. Neighbourhood

# In[16]:


plt.figure(figsize=(30,12))
fig = sns.countplot(x='neighbourhood',hue='no_show',data=df)
fig.set_xticklabels(fig.get_xticklabels(), rotation=90);


# ### It concludes that there's 81 Neighboorhoods and the highest number of patients showed up in 'JARDIM CAMBURI' hospital

# ###  2. Insurance

# In[17]:


ax = sns.countplot(x=df['scholarship'], hue=df['no_show'], data=df)
ax.set_title("Show & NoShow with and without Bolsa Família")
x_ticks_labels=['Scholarship', 'no Scholarship']
ax.set_xticklabels(x_ticks_labels)
plt.show()


# In[18]:


df['scholarship'].value_counts()


# ##### This graph shows that people who have no Scolarship are only 9.8 percent, but also there's no huge difference between the people who have no Scolarship to be showed up or not as seen on the graph.
# i.e, 90 percent have the Bosla Familia Scolarship which is great percent.

# In[19]:


df.info()


# In[20]:


df["Wait_days"] = df["appointmentday"] - df["scheduledday"]
df["Wait_days"] = df["Wait_days"].astype(str)
df["Wait_days"] = df["Wait_days"].apply(lambda x: x.split(" ")[0])
df["Wait_days"] = df["Wait_days"].astype(int)
df.head()


# In[21]:


df["Wait_days"].value_counts()


# In[22]:


# Exploring unreasonable wait days
drop_index = df[df["Wait_days"] < 0].index
df.drop(drop_index, inplace = True)

df[df["Wait_days"] < 0]


# In[37]:


# Time plot 
plt.figure(figsize=(30, 15)) 
plt.plot(df["Wait_days"]) 
plt.xlabel('Date') 
plt.ylabel('Number of Sunspots') 
plt.title('Monthly Sunspots Line Plot') 
plt.show() 


# In[35]:


# Seasonal plot 
plt.figure(figsize=(30, 15)) 
sns.lineplot(x=df.Wait_days, y=df['no_show'], ci=None) 
plt.xlabel('Month') 
plt.ylabel('no shows') 
plt.title('waiting time affecting no shows') 
plt.show() 


# In[ ]:




