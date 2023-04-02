# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:25:05 2020

@author: HP
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import urllib.request


class Vestige_bot(object):
    def __init__(self, PATH='./chromedriver'):
        """
        initialises bot.

        Parameters
        ----------
        PATH : str, optional
            path to the chromedriver. The default is './chromedriver'.

        Returns
        -------
        None.

        """
        self.driver=webdriver.Chrome(PATH)
        self.valid_prodIDs=[22001, 22002, 22003, 22004, 22005, 22006, 22007,
                            22009, 22010, 22011, 22013, 22014, 22016, 23001,
                            23002, 23003, 23004, 23005, 23006, 23007, 23008,
                            23009, 23010, 23011, 23014, 23015, 23016, 23017,
                            23018, 23019, 23020, 23021, 23022, 23023, 23024,
                            23025, 23026, 23029, 23030, 23031, 23032, 23033,
                            23034, 23035, 23036, 23037, 23038, 23039, 23040,
                            23041, 23042, 23043, 23044, 23045, 23046, 23047,
                            23048, 23049, 23050, 23051, 23052, 23053, 23054,
                            23055, 23056, 23057, 23058, 23059, 23060, 23061,
                            23066, 23067, 28000, 28001, 28002, 28003, 28004,
                            28007, 28008, 28009, 24003, 24004, 24006, 24007,
                            25001, 25002, 25003, 25006, 25008, 25009, 26002,
                            26004, 26005, 26006, 26007, 26008, 26009, 26011,
                            26012, 27001, 27002, 27003, 27004, 27005, 27006,
                            27007, 27009, 27010, 29005, 29006, 29007, 29008,
                            700, 701, 705, 710, 720, 730, 738, 740, 742, 750,
                            760, 765, 770, 780, 785, 800, 16001, 16058, 33104,
                            33105, 33106, 33109, 33110, 33113, 33114, 33115,
                            33116, 33117, 33118, 33119, 33120, 33121, 33122,
                            33123, 33124, 33001, 33002, 33006, 33008, 35101,
                            35102, 35103, 35152, 35153, 35155, 35156, 35159,
                            35160, 35303, 35304, 35305, 35203, 35205, 35401,
                            7301, 7302, 7305, 7401, 7402, 7403, 30001, 30002,
                            30003, 30005, 30006, 30007, 30008, 30009, 36001,
                            36002, 36003, 36004, 31101, 31102, 31103, 31104,
                            31105, 31106, 32501, 32502, 32503, 32504, 32505,
                            32506, 32507, 32508, 32509, 32510, 32511, 32512,
                            32513, 32514, 32515, 32516, 32517, 32518, 32519,
                            32520, 32521, 32522, 32523, 32524, 32525, 32526,
                            32527, 32528, 32529, 32530, 33301, 33302, 33303,
                            33304, 33305, 33306, 33307, 33308, 37005, 36101,
                            36102, 36103, 36104, 36105, 36106, 20001, 20002,
                            20004, 20005, 20007, 20008, 20009, 20010, 20011,
                            20012, 20013, 20014, 20015, 20016, 20017, 20020,
                            20021, 20023, 20024, 20025, 21001, 21002, 21004,
                            21005, 21006, 21008, 21009, 21011, 21012, 21013,
                            21016, 21017, 21018, 21019, 21020, 21021, 21022,
                            21023, 21026, 21027, 21028]
    
    def open_page(self):
        """
        Opens vestige website.

        Returns
        -------
        None.

        """
        
        self.driver.maximize_window()
        self.driver.get("http://shop.myvestige.com/")

    def login(self, distID = "55787455", password = "Anbu@123"):
        """
        logs into the vestige account with given credentials.

        Parameters
        ----------
        distID : int
            distributor ID.
        password : str
            password for the dist ID.

        Returns
        -------
        None.

        """
        
        login_button=self.driver.find_element("xpath", '//*[@id="header-account"]/div/ul/li/a')
        login_button.click()
        Dist_ID = self.driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/div/div/form/div/div/div[1]/ul/li[1]/div/input')
        Password = self.driver.find_element("xpath", '//*[@id="pass"]')
        Dist_ID.click()
        Dist_ID.send_keys(str(distID))
        Password.click()
        Password.send_keys(str(password))
        login_button=self.driver.find_element("xpath", '//*[@id="send2"]')
        login_button.click()
        
    def search_and_click(self, ProdID):
        """
        searches for the given ProdID and opens its product page. 

        Parameters
        ----------
        ProdID : int 
            Product ID of the product needed.

        Returns
        -------
        None.

        """
        search_field=self.driver.find_element_by_xpath('//*[@id="search"]')
        search_field.click()
        for i in range(6):
            search_field.send_keys(Keys.BACKSPACE)
        search_field.send_keys(ProdID)
        search_button=self.driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[1]/button')
        search_button.click()
        self.driver.execute_script("window.scrollTo(0, 256)") 
        thing=self.driver.find_element_by_xpath('//*[@id="top"]/body/div[1]/div/div[2]/div/div[3]/div[2]/ul/li/div/h2/a')
        thing.click()
        self.driver.execute_script("window.scrollTo(0, 256)") 
        
    def exit_bot(self):
        """
        exits browser.

        Returns
        -------
        None.

        """
        self.driver.close()
        
    def find_prices(self):
        """
        Finds the prices of the product and PV when you are in the 
        product page. 
        
        Returns  
        -------
        a dictionary of the Dist price (DP) and MRP and PV.

        """
        url=self.driver.current_url
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source,'lxml')
        List = soup.find_all("span", class_="price")
        Dict={}
        MRP=List[0].string[2:]
        DP=List[1].string[2:]
        def remove_comma(y):
            """
            removes commas from  the given string

            Parameters
            ----------
            y : string
                string from which commas have to be removed.

            Returns
            -------
            x : string
                result after removin all commas from y.

            """
            x=y
            while "," in x:
                List = list(x)
                List.remove(",")
                Str=""
                for i in List: 
                    Str+=i
                x=Str
            return x
        DP = remove_comma(DP)
        MRP = remove_comma(MRP)
        Dict["MRP"]=float(MRP)
        Dict["DP"]=float(DP)
        PV = float(soup.find("p", class_="pv").string[5:])
        Dict["PV"]=PV
        Name=soup.find("span", class_="h1").string
        Dict["Name"]=Name
        return Dict
    
    def get_prod_info(self, ProdID):
        """
        

        Parameters
        ----------
        ProdID : int
            Product ID.

        Returns
        -------
        Dict : dict
            Dictionary connecting the ProdID to a dict of MRP, DP and PV.

        """
        self.search_and_click(ProdID)
        Dict={}
        Dict[ProdID]=self.find_prices()
        return Dict
    
    
    def add_distributor(self, infoDict = None):
        """
        

        Parameters
        ----------
        infoDict : dict, optional
            dict containing info for adding distributor. The default is get_infoDict().

        Returns
        -------
        None.

        """
        
        def get_infoDict():
            """
            builds infoDict from user input.
    
            Returns
            -------
            infoDict : dict
                infoDict for adding distributor.
    
            """
            vals=['UID', 'First Name', 'Last Name', 'Adress', 'Mobile', 'Email', 'Pincode']
            infoDict={}
            for i in vals:
                Input=str(input("Enter "+ i+ ":\n"))
                infoDict[i]=Input
                if Input == "None":
                    infoDict[i]=""
            return infoDict
        
        if infoDict==None:
            infoDict=get_infoDict()
        
        self.driver.get('https://shop.myvestige.com/index.php/distributor-registration/')
        self.driver.execute_script("window.scrollTo(0, 2160)")
        time.sleep(0.1)
        delaytime=4
        self.driver.execute_script("window.scrollTo(0, 0)") 
        uplineID=self.driver.find_element_by_xpath('//*[@id="upline_no"]')
        uplineID.send_keys(str(infoDict["UID"]))
        country=self.driver.find_element_by_xpath('//*[@id="select_country"]')
        country.click()
        time.sleep(delaytime)
        distID=self.driver.find_element_by_xpath('//*[@id="distributor_nos"]')
        distID.click()
        time.sleep(delaytime)
        title=self.driver.find_element_by_xpath('//*[@id="distributor_title"]')
        title.click()
        time.sleep(delaytime)
        firstName=self.driver.find_element_by_xpath('//*[@id="distributor_first_name"]')
        firstName.click()
        firstName.send_keys(infoDict["First Name"])
        lastName=self.driver.find_element_by_xpath('//*[@id="distributor_last_name"]')
        lastName.click()
        lastName.send_keys(infoDict["Last Name"])
        gender=self.driver.find_element_by_xpath('//*[@id="dist_gender"]')
        gender.click()
        time.sleep(delaytime)
        adress=self.driver.find_element_by_xpath('//*[@id="address_1"]')
        adress.click()
        adress.send_keys(infoDict["Adress"])
        mobile=self.driver.find_element_by_xpath('//*[@id="mobile"]')
        mobile.click()
        mobile.send_keys(infoDict["Mobile"])
        email=self.driver.find_element_by_xpath('//*[@id="email"]')
        email.click()
        email.send_keys(infoDict["Email"])
        pincode=self.driver.find_element_by_xpath('//*[@id="pin_no"]')
        pincode.click()
        pincode.send_keys(infoDict["Pincode"])
        
    def add_to_cart(self, prodDict=None):
        
        def get_prodDict():
            state=True
            prodDict={}
            while state:
                prodId=str(input("Enter prodID:\n"))
                if prodId.lower()=="none":
                    state=False
                    break
                qty=str(input("Enter qty:\n"))
                prodDict[int(prodId)]=int(qty)
            return prodDict
        if prodDict==None:
            prodDict=get_prodDict()
        
        prodIDs=[]
        for i in prodDict.keys():
            prodIDs.append(i)
        for prodID in prodIDs:
            try:
                self.search_and_click(prodID)
                qty_button=self.driver.find_element_by_xpath('//*[@id="qty"]')
                add_button=self.driver.find_element_by_xpath('//*[@id="product_addtocart_form"]/div[4]/div/div/div[2]/button')
                qty_button.click()
                qty_button.send_keys(Keys.ARROW_RIGHT)
                qty_button.send_keys(Keys.BACKSPACE)
                qty_button.send_keys(prodDict[prodID])
                add_button.click()
            except:
                print("Error tryig to execute productID=", prodID)
                
        
        return
        
        

bot=Vestige_bot()
bot.open_page()
bot.login()
time.sleep(10)
#l=[22001, 22002, 22003, 22004, 22005, 22006, 22007, 22009, 22010, 22011, 22013, 22014, 22016, 23001, 23002, 23003, 23004, 23005, 23006, 23007, 23008, 23009, 23010, 23011, 23014, 23015, 23016, 23017, 23018, 23019, 23020, 23021, 23022, 23023, 23024, 23025, 23026, 23029, 23030, 23031, 23032, 23033, 23034, 23035, 23036, 23037, 23038, 23039, 23040, 23041, 23042, 23043, 23044, 23045, 23046, 23047, 23048, 23049, 23050, 23051, 23052, 23053, 23054, 23055, 23056, 23057, 23058, 23059, 23060, 23061, 23066, 23067, 28000, 28001, 28002, 28003, 28004, 28007, 28008, 28009, 24003, 24004, 24006, 24007, 25001, 25002, 25003, 25006, 25008, 25009, 26002, 26004, 26005, 26006, 26007, 26008, 26009, 26011, 26012, 27001, 27002, 27003, 27004, 27005, 27006, 27007, 27009, 27010, 29005, 29006, 29007, 29008, 700, 701, 705, 710, 720, 730, 738, 740, 742, 750, 760, 765, 770, 780, 785, 800, 16001, 16058, 33104, 33105, 33106, 33109, 33110, 33113, 33114, 33115, 33116, 33117, 33118, 33119, 33120, 33121, 33122, 33123, 33124, 33001, 33002, 33006, 33008, 35101, 35102, 35103, 35152, 35153, 35155, 35156, 35159, 35160, 35303, 35304, 35305, 35203, 35205, 35401, 7301, 7302, 7305, 7401, 7402, 7403, 30001, 30002, 30003, 30005, 30006, 30007, 30008, 30009, 36001, 36002, 36003, 36004, 31101, 31102, 31103, 31104, 31105, 31106, 32501, 32502, 32503, 32504, 32505, 32506, 32507, 32508, 32509, 32510, 32511, 32512, 32513, 32514, 32515, 32516, 32517, 32518, 32519, 32520, 32521, 32522, 32523, 32524, 32525, 32526, 32527, 32528, 32529, 32530, 33301, 33302, 33303, 33304, 33305, 33306, 33307, 33308, 37005, 36101, 36102, 36103, 36104, 36105, 36106, 20001, 20002, 20004, 20005, 20007, 20008, 20009, 20010, 20011, 20012, 20013, 20014, 20015, 20016, 20017, 20020, 20021, 20023, 20024, 20025, 21001, 21002, 21004, 21005, 21006, 21008, 21009, 21011, 21012, 21013, 21016, 21017, 21018, 21019, 21020, 21021, 21022, 21023, 21026, 21027, 21028]

#Dict={}
#for i in l:
#    Dict+=bot.get_prod_info(i)
#bot.exit_bot()
#print(Dict)
#print(len(bot.valid_prodIDs))
