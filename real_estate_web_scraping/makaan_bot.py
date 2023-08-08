# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:50:26 2022

@author: aldis
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import urllib.request

class makaan_bot():
    def __init__(self, path = "./chromedriver", num_pages = 3000):
        """
        

        Parameters
        ----------
        path : str, optional
            path to chromedriver.exe. The default is "./chromedriver".
        num_pages : int, optional
            number of pages to search in search query. The default is 3000.

        Returns
        -------
        None.

        """
        self.driver = webdriver.Chrome(path)
        self.info_dict = dict()
        self.num_pages = num_pages
        
    def get_page(self, base = "https://www.makaan.com/chennai-residential-property/buy-property-in-chennai-city?page = ", page = 1):
        """
        

        Parameters
        ----------
        base : str, optional
            search results to scrape. The default is "https://www.makaan.com/chennai-residential-property/buy-property-in-chennai-city?page = ".
        page : TYPE, optional
            page number of saerch results. The default is 1.

        Returns
        -------
        None.

        """
        
        
        
        
        self.driver.get(base + str(page))    
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("window.scrollTo(0, 0);")
    
    def get_listings(self):
        """
        

        Returns
        -------
        list
            list of html of all listings in current page of self.driver.

        """
        url = self.driver.current_url
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source,'lxml')
        return soup.find_all("div", class_="cardLayout clearfix")
    
    def get_digits(self, string):
        """
        

        Parameters
        ----------
        string : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """        
        
        temp = ""
        for char in string:
            if char.isdigit():
                temp += char
        return temp.strip()
            
    
    def get_info(self, listing):
        
        latitude = listing.find("meta", itemprop = "latitude").get("content")
        longitude = listing.find("meta", itemprop = "longitude").get("content")
        
        title_line = listing.find("div", class_ = "title-line")
        property_type = title_line.find("strong").get_text()
        
        url = listing.find("meta", itemprop = "url").get("content")
        
        price = listing.find("meta", itemprop = "price").get("content")
        price_currency = listing.find("meta", itemprop = "priceCurrency").get("content")
        
        sq_ft_rate = listing.find("td", class_ = "lbl rate").get_text()
        sq_ft_rate = self.get_digits(sq_ft_rate)
        
        sq_ft_area = listing.find("td", class_ = "size").get_text()
        
        status = listing.find("td", class_ = "val").get_text()
        
        proj_name = listing.find("a", class_ = "projName").get_text()
        
        rera = False
        
        if listing.find("div", class_ = "rera-tag-new"):
            rera = True
        
        locality = listing.find("span", itemprop = "addressLocality").get_text()
        
        city = listing.find("span", class_ = "cityName").get_text()
                
        d = dict()
        
        d["latitude"] = latitude
        d["longitude"] = longitude
        d["property_type"] = property_type
        d["url"] = url
        d["price"] = price
        d["curency"] = price_currency
        d["Area_sqft"] = sq_ft_area
        d["sqft_rate"] = sq_ft_rate
        d["status"] = status
        d["proj_name"] = proj_name
        d["rera_approval"] = rera
        d["city"] = city
        d["locality"] = locality
        
        print(d)
        
        return d
        
        
        
                                
bot = makaan_bot()
bot.get_page()
bot.get_info(bot.get_listings()[0])      