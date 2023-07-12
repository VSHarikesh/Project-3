from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# To use the Python Selenium Selector you have to use the By class
from selenium.webdriver.common.by import By

class Hari:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    Street1 = '1/248,Gandhi nagar,Chennai-600001'
    City = 'Chennai'
    State = 'Tamilnadu'
    Zipcode = '600001'
    Mobile = '6578239710'
    Work_Email = 'abc@gmail.com'
    
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
    # Contact details locator as XPATH
    Contactdetails_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
    # Street1 locator as XPATH
    Street1_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    # City locator as XPATH
    City_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    # State locator as XPATH
    State_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    # Zip code locator as XPATH
    Zipcode_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    # Mobile locator as XPATH
    Mobile_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    # Work email locator as XPATH
    Work_Email_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    # Save button locator as XPATH
    Savebutton_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
    
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
        
    # Method for Contact Details page
    def Contact_Details(self):
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.Contactdetails_locator).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.Street1_locator).send_keys(self.Street1)
        self.driver.find_element(by=By.XPATH, value=self.City_locator).send_keys(self.City)
        self.driver.find_element(by=By.XPATH, value=self.State_locator).send_keys(self.State)
        self.driver.find_element(by=By.XPATH, value=self.Zipcode_locator).send_keys(self.Zipcode)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.Mobile_locator).send_keys(self.Mobile)
        self.driver.find_element(by=By.XPATH, value=self.Work_Email_locator).send_keys(self.Work_Email)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.Savebutton_locator).click()
        # Bug removal
        while(True):
            pass
 
Hari().Browsing()
Hari().login()
Hari().PIM_page()
Hari().Employee_list()
Hari().Contact_Details()    
