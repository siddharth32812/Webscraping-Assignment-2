#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT-2

# Ans-5

# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[2]:


driver=webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32./chromedriver.exe')


# In[3]:


url='https://www.flipkart.com/'
driver.get(url)


# In[4]:


search_iphone_11=driver.find_element_by_class_name("_3704LK")
search_iphone_11


# In[5]:


search_iphone_11.send_keys("iphone_11")


# In[6]:


search_btn=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_btn


# In[7]:


search_btn.click()


# In[8]:


title_tags=driver.find_elements_by_xpath('//div[@class="_4rR01T"]')
title_tags


# In[12]:


#Taking the empty lists
Rating=[]
review=[]
full_summary=[]

#As there are 10 reviews per page, we will check for 10 pages and scrap the required data
#Now we will take a for loop and scrap
for i in range(0,11):
    for j in driver.find_elements_by_xpath("//div[@class='_3LWZlK _1BLPMq']"):
        Rating.append(j.text)
    for j in driver.find_elements_by_xpath("//p[@class='_2-N8zT']"):
        review.append(j.text)
    for j in driver.find_elements_by_xpath("//div[@class='t-ZTKy']"):
        full_summary.append(j.text)
        
    #Path for next page as it changes for every page. We are appending numbers as pages change  
    k=i+1
    next_page="https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/product-reviews/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART&page="+str(k) 
    driver.get(next_page)
     


# In[13]:


Rating


# In[14]:


review


# In[15]:


full_summary


# In[17]:


print(len(Rating),len(review),len(full_summary))


# In[18]:


phone=pd.DataFrame({})
phone['Rating']=Rating[:100]
phone['Review']=review[:100]
phone['Full summary']=full_summary[:100]
phone


# In[20]:


phone.to_csv('Flipkart_iphoneReviews.csv')


# In[21]:


driver.close()


# In[ ]:




