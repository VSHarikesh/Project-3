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
    Firstname = 'Z.Radha'
    Lastname = 'Krishna'
    PIM_username = 'Radhakrishna'
    PIM_password = 'Radhakrishna1812'
    PIM_confirmpassword = 'Radhakrishna1812'
    
    # username_locator is a TagName
    username_locator = 'username'
    # password_locator is a TagName
    password_locator = 'password'
    # Submit Button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    # Adminpage_locator as XPATH
    Adminpage_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    # PIMpage_locator as XPATH
    PIMpage_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    # Add+ button locator as XPATH
    Add_button_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    # Add employee Firstname_locator as TagName
    Firstname_locator = 'firstName'
    # Lastname_locator as TagName
    Lastname_locator = 'lastName'
    # Radiobutton_locator as XPATH
    Radiobutton_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    # PIM username locator as XPATH
    PIM_username_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    # PIM password locator as XPATH
    PIM_password_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    # PIM confirmpassword locator as XPATH
    PIM_confirmpassword_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    # PIM Savebutton locator as XPATH
    PIM_savebutton_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    
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
        sleep(3)
        #self.driver.implicitly_wait(15)
        self.driver.find_element(by=By.XPATH, value=self.Adminpage_locator).click()
        
    # Method for PIM page
    def PIM_page(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.PIMpage_locator).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.Add_button_locator).click()
    
    # Method for Adding employee
    def Add_employee(self):
        sleep(3)
        self.driver.find_element(by=By.NAME, value=self.Firstname_locator).send_keys(self.Firstname)
        self.driver.find_element(by=By.NAME, value=self.Lastname_locator).send_keys(self.Lastname)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.Radiobutton_locator).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.PIM_username_locator).send_keys(self.PIM_username)
        self.driver.find_element(by=By.XPATH, value=self.PIM_password_locator).send_keys(self.PIM_password)
        self.driver.find_element(by=By.XPATH, value=self.PIM_confirmpassword_locator).send_keys(self.PIM_confirmpassword)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.PIM_savebutton_locator).click()
       #Bug removal
        while(True):
            pass

Hari().Browsing()
Hari().login()
Hari().Admin_page()
Hari().PIM_page()
Hari().Add_employee()

