#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT-2

# Ans-7

# In[5]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[6]:


driver=webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32./chromedriver.exe')


# In[7]:


url='https://www.myntra.com/shoes'
driver.get(url)


# In[8]:


sneakers_prc=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label/div')
sneakers_prc


# In[9]:


sneakers_prc.click()


# In[11]:


sneakers_clr=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label/div')
sneakers_clr


# In[12]:


sneakers_clr.click()


# In[22]:


brand=[]
short_desc=[]
price=[]

#We can see that there are 50 products in one page, and as we need to scrap for 100 products, we need to take 2 pages data
for i in range(0,2):
    #Finding the tags having the brand name
    for j in driver.find_elements_by_xpath("//h3[@class='product-brand']"):
        brand.append(j.text) #Extracting text from tags and appending to emptylist
    
    #Finding the tags having short description of the shoe
    for j in driver.find_elements_by_xpath("//h4[@class='product-product']"):
        short_desc.append(j.text) #Extracting text from tags and appending to emptylist
        
    #Finding the tags having the price of the shoe
    for j in driver.find_elements_by_xpath("//div[@class='product-price']"):
        price.append(j.text)  #Extracting text from tags and appending to emptylist


# In[23]:


brand


# In[24]:


short_desc


# In[25]:


price


# In[26]:


shoes=pd.DataFrame({})
shoes['Brand Name']=brand
shoes['Short Description']=short_desc
shoes['Price']=price
shoes


# In[27]:


shoes.to_csv('Myntra_shoes.csv')


# In[28]:


driver.close()


# In[ ]:




