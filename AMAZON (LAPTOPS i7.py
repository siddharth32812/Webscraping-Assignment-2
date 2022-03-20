#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT-2

# Ans-8

# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[4]:


driver=webdriver.Chrome(r'C:/Users/Admin/Downloads/chromedriver_win32./chromedriver.exe')


# In[6]:


url='https://www.amazon.in/'
driver.get(url)


# In[9]:


search_laptops=driver.find_element_by_id('twotabsearchtextbox')
search_laptops


# In[10]:


search_laptops.send_keys("laptops")


# In[11]:


search_btn=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]')
search_btn


# In[12]:


search_btn.click()


# In[13]:


cpu_i7=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[12]/span/a/div')
cpu_i7


# In[14]:


cpu_i7.click()


# In[17]:


title_tags=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
title_tags


# In[18]:


prod_title=[]
for i in title_tags[:10]:
    prod_title.append(i.text)
prod_title


# In[20]:


price=driver.find_elements_by_xpath("//span[@class='a-price']")
price


# In[21]:


prod_price=[]
for i in price[:10]:
    prod_price.append(i.text)
prod_price


# In[ ]:




