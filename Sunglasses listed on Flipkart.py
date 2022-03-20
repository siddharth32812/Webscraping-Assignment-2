#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT-2

# Ans-4) Sunglasses listed on flipkart

# In[33]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[34]:


driver=webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32./chromedriver.exe')


# In[35]:


url='https://www.flipkart.com/'
driver.get(url)


# In[36]:


search_sunglasses=driver.find_element_by_class_name("_3704LK")
search_sunglasses


# In[37]:


search_sunglasses.send_keys("sunglasses")


# In[38]:


search_btn=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_btn


# In[39]:


search_btn.click()


# In[40]:


title_tags=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
len(title_tags)
title_tags


# In[43]:


brand=[]
for i in title_tags:
    brand.append(i.text)
brand


# In[47]:


product_description=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
len(product_description)
product_description


# In[48]:


prod_desc=[]
for i in product_description:
    prod_desc.append(i.text)
prod_desc


# In[49]:


discounted_prc=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
discounted_prc


# In[50]:


price=[]
for i in discounted_prc:
    price.append(i.text)
price


# In[52]:


discount=driver.find_elements_by_xpath('//div[@class="_3Ay6Sb"]')
discount


# In[54]:


disc=[]
for i in discount:
    disc.append(i.text)
disc


# In[56]:


print(len(brand),len(prod_desc),len(price),len(disc))


# In[58]:


sunglasses=pd.DataFrame()
sunglasses['Brand']=brand
sunglasses['Product Description ']=prod_desc
sunglasses['Discounted Price']=price
sunglasses['Discount']=disc
sunglasses


# In[59]:


sunglasses.to_csv("Sunglasses listed on Flipkart.csv")


# In[60]:


driver.close()


# In[ ]:




