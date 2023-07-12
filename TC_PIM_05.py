from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# To use the Python Selenium Selector you have to use the By class
from selenium.webdriver.common.by import By
# Python Selenium SELECT class - It is used for Dropdowns and to select multiple things
from selenium.webdriver.support.ui import Select

class Hari:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    Nickname = 'Radhakrishna'
    Licensenumber = '348792356'
    Expirydate = '2023-12-30'
    SSNnumber = '45622455'
    SINnumber = '56498584'
    DOB = '2000-10-20'
    Militaryservice = 'No'
   
    
    # username_locator is a TagName
    username_locator = 'username'
    # password_locator is a TagName
    password_locator = 'password'
    # Submit Button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    # PIMpage_locator as XPATH
    PIMpage_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'    
    # Employeelist_locator as XPATH
    Employeelist_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]'
     # Personal details-> Nickname locator as XPATH
    Nickname_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    # License number locator as XPATH
    Licensenumber_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    # Expiry date locator as XPATH
    Expirydate_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    # SSN no. locator as XPATH
    SSNnumber_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    # SIN no. locator as XPATH
    SINnumber_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    # DOB locator as XPATH
    DOB_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    # Gender locator as XPATH
    Gender_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    # Military service locator as XPATH
    Militaryservice_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    # Save button locator as XPATH
    Savebutton_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    #
    Nationality_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/i'
    
# Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Method for login into the CRM application
    def login(self):
        sleep(2)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()
    
    # Method for PIM page
    def PIM_page(self):
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.PIMpage_locator).click()
    
    # Method for Employee list page
    def Employee_list(self):
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.Employeelist_locator).click() 
    
     # Method for Personal Details page
    def Personal_details(self):
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.Nickname_locator).send_keys(self.Nickname)
        self.driver.find_element(by=By.XPATH, value=self.Licensenumber_Locator).send_keys(self.Licensenumber)
        self.driver.find_element(by=By.XPATH, value=self.Expirydate_locator).send_keys(self.Expirydate)
        self.driver.find_element(by=By.XPATH, value=self.SSNnumber_locator).send_keys(self.SSNnumber)
        self.driver.find_element(by=By.XPATH, value=self.SINnumber_locator).send_keys(self.SINnumber)
        self.driver.find_element(by=By.XPATH, value=self.DOB_locator).send_keys(self.DOB)
        self.driver.find_element(by=By.XPATH, value=self.Gender_locator).click()
        self.driver.find_element(by=By.XPATH, value=self.Militaryservice_locator).send_keys(self.Militaryservice)
        
    def select_Nationality(self):
        print('Method - select_Nationality')
        sleep(3)
        Nationality = self.driver.find_element(by=By.CLASS_NAME, value='oxd-select-text-input')
        Nationality_dropdown = Select(Nationality)
        Nationality_dropdown.select_by_index('1')
        self.driver.find_element(by=By.XPATH, value=self.Savebutton_locator).click()
    
      
     # Bug removal
        while(True):
            pass
        
Hari().Browsing()
Hari().login()
Hari().PIM_page()
Hari().Employee_list()
Hari().Personal_details()
Hari().select_Nationality()