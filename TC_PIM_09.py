from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# To use the Python Selenium Selector you have to use the By class
from selenium.webdriver.common.by import By
# Python Selenium SELECT class - It is used for Dropdowns and to select multiple things
from selenium.webdriver.support.ui import Select 

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

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
    # JobDetails_locator as 
    JobDetails_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    #
    JobTitle_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]'
    
    
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
        
    # Method for Job details page
    def Job_Details(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.JobDetails_locator).click()
    
    #   
    def Job_Title(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.JobTitle_locator).click()
    
        
        #dropdown_element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'oxd-select-text-input')))
        #sleep(30)
        #dropdown = Select(dropdown_element)
        #dropdown.select_by_visible_text("Account Assistant")
        #Bug removal
        #while(True):
            #pass
        
        #Job_Title = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]')
        #sleep(2)
        #Job_Title.click()
    
    #
    # def select_Job_Title(self):
    #     print('Method - select_Job_Title')
    #     sleep(5)
    #     Jobtitle = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]')
    #     JobTitle_dropdown = Select(Jobtitle)
    #     JobTitle_dropdown.select_by_index(6)
    #     # Bug removal
    #     while(True):
    # #     #    pass
        
        

Hari().Browsing()
Hari().login()
Hari().PIM_page()
Hari().Employee_list()
Hari().Job_Details()
Hari().Job_Title()
