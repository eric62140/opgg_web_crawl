#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import requests


# In[26]:


heroes = pd.read_csv("league_heroes.csv")
for col in heroes.columns:
    heroes[col].values[:] = 0
heroes['Annie'] = 0


# In[5]:


url = "http://www.op.gg/summoner/userName=destiny"
url2 = "http://www.op.gg/summoner/userName=sktt1kuri"

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url2)

for i in range(1,51):
    python_button = driver.find_element_by_xpath("// a[contains(text(),'Show More')][@href='#']")
    python_button.click()


# In[6]:


soup=BeautifulSoup(driver.page_source, 'lxml')    
champion_name = soup.find_all(attrs={'class': re.compile("Image20 __sprite __spc20 __spc20-")})
result = soup.find_all(attrs={'class': re.compile("GameResult")})
gtype = soup.find_all(attrs={'class': re.compile("GameType")})


# In[30]:


game_result = []
game22 = []
gametype=[]
for index, item in enumerate(result[:]):
    game_result.append(item.text.strip())
for index, item in enumerate(gtype):
    gametype.append(item.text.strip())
test = [0 for i in range(10)]
for i in range(50000):
    game22.append(test)
heroes[:] = 0


# In[31]:


k = 0
i = 0
q = 0
for k in range(0,10200,10):
    for index, item in enumerate(champion_name[k:k+10]):
        game22[i][q] = item.text.strip()
        q = q+1    
    gamelist = game22[i]
#     print(gamelist)
    for champ in gamelist:
        for names in heroes:
            if champ == names:
                heroes[names][i] = 1
                
    if game_result[i] == 'Defeat':
        for name in gamelist[:5]:
            for names in heroes:
                if name == names:
                    heroes[names][i] = 0
                    
    else:
        for name in gamelist[5:10]:
            for names in heroes:
                if name == names:
                    heroes[names][i] = 0
                    
    i = i+1               
    q = 0


# In[33]:


heroes['result'] = game_result
heroes['gametype'] = gametype


# In[36]:


heroes.to_csv('game1020.csv')

