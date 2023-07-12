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
    searchinput = 'directory'
    
    # username_locator is a TagName
    username_locator = 'username'
    # password_locator is a TagName
    password_locator = 'password'
    # Submit Button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    # Adminpage locator as XPATH
    Adminpage_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    # User management locator as XPATH
    Usermanagement_locator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    # Users locator as XPATH
    Users_locator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a'
    
    # Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Method for login into the CRM application
    def login(self):
        sleep(3)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()
        
    # Method for Adminpage 
    def Admin_page(self):
        sleep(5)
        #self.driver.implicitly_wait(15)
        self.driver.find_element(by=By.XPATH, value=self.Adminpage_locator).click()
        
    # Method for User Management in header
    def User_management(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.Usermanagement_locator).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.Users_locator).click()
        # Bug removal
        while(True):
            pass

Hari().Browsing()
Hari().login()
Hari().Admin_page()
Hari().User_management()
