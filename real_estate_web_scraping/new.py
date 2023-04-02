# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:22:18 2022

@author: aldis
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import urllib.request

driver = webdriver.Chrome("./chromedriver")
tot_List = []
for i in range(5000):
    driver.get("https://www.makaan.com/chennai-residential-property/buy-property-in-chennai-city?page="+str(i+1))
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    url=driver.current_url
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')
    # List1 = soup.find_all("script", attrs = {"type": "text/x-config"})
    # for item in List1:
    #     if "totalCount" in item.get_text():
    #         print(item)
    # time.sleep(10)
    List = soup.find_all("div", class_="cardLayout clearfix")
    tot_List.extend(List)
    if len(tot_List) >= 687:
        print(len(List))
        break
        