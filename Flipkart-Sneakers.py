#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT-2

# ANS-6

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


search_sneakers=driver.find_element_by_class_name("_3704LK")
search_sneakers


# In[5]:


search_sneakers.send_keys("sneakers")


# In[6]:


search_btn=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_btn


# In[7]:


search_btn.click()


# In[24]:


brand=[]
prod_desc=[]
disc_price=[]

#We need to scrap for 100 products and here we will consider the data from first 3 pages
#We will take a for loop and scrap data from all the pages
for i in range(0,4):
    for j in driver.find_elements_by_xpath("//div[@class='_2WkVRV']"):
        brand.append(j.text)
    for j in driver.find_elements_by_xpath("//a[@class='IRpwTa']"):
        prod_desc.append(j.text)
    for j in driver.find_elements_by_xpath("//div[@class='_30jeq3']"):
        disc_price.append(j.text)
   
    #Path for next page as it changes for every page. We are appending numbers as pages change  
    k=i+2
    next_page="https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(k)
    driver.get(next_page)
    


# In[25]:


brand


# In[26]:


prod_desc


# In[27]:


disc_price


# In[29]:


print(len(brand),len(prod_desc),len(disc_price))


# In[30]:


sneakers=pd.DataFrame({})
sneakers['Brand']=brand[:100]
sneakers['Description']=prod_desc[:100]
sneakers['Discounted Price']=disc_price[:100]
sneakers


# In[31]:


sneakers.to_csv('Flipkart_sneakers.csv')


# In[32]:


driver.close()


# In[ ]:




