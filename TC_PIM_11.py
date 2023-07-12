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
        #Bug removal
        while(True):
            pass

Hari().Browsing()
Hari().login()
Hari().PIM_page()
Hari().Employee_list()
