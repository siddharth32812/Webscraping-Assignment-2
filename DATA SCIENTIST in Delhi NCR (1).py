#!/usr/bin/env python
# coding: utf-8

# Ans-1

#  A python program to scrape data for “Data Analyst” Job position in “Bangalore” location.

# In[4]:


get_ipython().system('pip install selenium')


# In[15]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[16]:


driver=webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32/chromedriver.exe')


# In[17]:


url='https://www.naukri.com/'
driver.get(url)


# In[18]:


search_job=driver.find_element_by_class_name("suggestor-input" )
search_job


# In[19]:


search_job.send_keys("Data Analyst")


# In[20]:


search_locn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_locn


# In[21]:


search_locn.send_keys("Bangalore")


# In[24]:


search_btn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_btn


# In[25]:


search_btn.click()


# In[26]:


salary_check=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[4]/div[2]/div[1]/label/i')
salary_check


# In[27]:


salary_check.click()


# In[28]:


title_tags=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(title_tags)
title_tags[0:10]


# In[34]:


job_titles=[]
for i in title_tags:
    job_titles.append(i.text)
len(job_titles)
job_titles[0:10]


# In[36]:


company_tags=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
company_tags[0:10]


# In[37]:


company_names=[]
for i in company_tags:
    company_names.append(i.text)
company_names[0:10]


# In[39]:


exp_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]')
len(exp_tags)


# In[41]:


experience=[]
for i in exp_tags:
    experience.append(i.text)
experience[:10]


# In[42]:


locn_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(locn_tags)


# In[44]:


location=[]
for i in locn_tags:
    location.append(i.text)
location[:10]


# In[46]:


len(job_titles),len(company_names),len(experience),len(location)


# In[48]:


jobs=pd.DataFrame()
jobs['Job Title']=job_titles[:10]
jobs['Company']=company_names[:10]
jobs['experience']=experience[:10]
jobs['Location']=location[:10]
jobs


# In[49]:


jobs.to_csv('Data Analyst_Bangalore_Naukri.com.csv')


# In[50]:


driver.close()


# ASSIGNMENT-2

# Ans-2

# In[91]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[92]:


driver=webdriver.Chrome(r'C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe')


# In[93]:


url='https://www.naukri.com/'
driver.get(url)


# In[94]:


search_job=driver.find_element_by_class_name("suggestor-input ")
search_job


# In[95]:


search_job.send_keys("Data Scientist" )


# In[96]:


search_locn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_locn


# In[97]:


search_locn.send_keys("Delhi NCR")


# In[98]:


search_btn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_btn


# In[99]:


search_btn.click()


# In[100]:


title_tags=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(title_tags)
title_tags[:10]


# In[101]:


job_titles=[]
for i in title_tags:
    job_titles.append(i.text)
len(job_titles)
job_titles[:10]


# In[102]:


company_tags=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
company_tags[:10]


# In[103]:


company_names=[]
for i in company_tags:
    company_names.append(i.text)
company_names[:10]
    


# In[104]:


exp_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]')
len(exp_tags)


# In[105]:


experience=[]
for i in exp_tags:
    experience.append(i.text)
experience[:10]


# In[106]:


locn_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(locn_tags)


# In[107]:


location=[]
for i in locn_tags:
    location.append(i.text)
location[:10]


# In[108]:


len(job_titles),len(company_names),len(experience),len(location)


# In[109]:


jobs=pd.DataFrame()
jobs['Job Title']=job_titles[:10]
jobs['Company']=company_names[:10]
jobs['Experience']=experience[:10]
jobs['location']=location[:10]
jobs


# In[110]:


jobs.to_csv("Data Scientist in Delhi NCR.csv")


# In[111]:


driver.close()


# ASSIGNMENT-2

# Ans-3

# In[112]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[113]:


driver=webdriver.Chrome(r'C:/Users/Admin/Downloads/chromedriver_win32/chromedriver.exe')


# In[114]:


url='https://www.naukri.com/'
driver.get(url)


# In[115]:


search_job=driver.find_element_by_class_name("suggestor-input ")
search_job


# In[116]:


search_job.send_keys("Data Scientist" )


# In[117]:


search_locn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_locn


# In[118]:


search_locn.send_keys("Delhi NCR")


# In[119]:


search_btn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_btn


# In[120]:


search_btn.click()


# In[121]:


title_tags=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(title_tags)
title_tags[:10]


# In[122]:


job_titles=[]
for i in title_tags:
    job_titles.append(i.text)
len(job_titles)
job_titles[:10]


# In[123]:


company_tags=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
company_tags[:10]


# In[124]:


company_names=[]
for i in company_tags:
    company_names.append(i.text)
company_names[:10]


# In[125]:


exp_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]')
len(exp_tags)


# In[126]:


experience=[]
for i in exp_tags:
    experience.append(i.text)
experience[:10]


# In[127]:


locn_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(locn_tags)


# In[128]:


location=[]
for i in locn_tags:
    location.append(i.text)
location[:10]


# In[129]:


len(job_titles),len(company_names),len(experience),len(location)


# In[130]:


jobs=pd.DataFrame()
jobs['Job Title']=job_titles[:10]
jobs['Company']=company_names[:10]
jobs['Experience']=experience[:10]
jobs['location']=location[:10]
jobs


# In[131]:


jobs.to_csv("Data Scientist in Delhi NCR.csv")


# In[132]:


driver.close()


# In[ ]:




