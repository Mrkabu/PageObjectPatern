from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import Locators
from selenium.webdriver.common.keys import Keys
import time

class Testy():

    def __init__(self):
        self.driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://ncplusgo.pl')

    def zalogujiwyszukaj(self):

        self.driver.find_element(By.XPATH, Locators.logo).click()
        self.driver.find_element(By.XPATH, Locators.rozumiem).click()
        #self.driver.find_element(By.XPATH, Locators.terazwtv).click()
        self.driver.find_element(By.XPATH, Locators.login).send_keys('jakub.karol.kucharski@gmail.com')
        self.driver.find_element(By.XPATH, Locators.password).send_keys('Hasloncplusgo@123')
        self.driver.find_element(By.XPATH, Locators.buttonzaloguj).click()
        self.driver.find_element(By.XPATH, Locators.logowyszukiwarka).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Locators.wyszukiwarka).send_keys('Kruk' + Keys.ENTER)

        k = self.driver.find_element(By.XPATH, Locators.kruk)

        if k.is_displayed:
            print("OK")

    def test2(self):

        self.driver.find_element(By.XPATH, Locators.terazwtv).click()

run = Testy()
run.zalogujiwyszukaj()