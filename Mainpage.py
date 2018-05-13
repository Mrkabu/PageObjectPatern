from Locators import Locators #import z piku Locators.py gdzie definiujemy obiekty
from selenium.webdriver.common.by import By
from selenium import webdriver

class Home(object):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://ncplusgo.pl')
        return self.driver


    def getLogo(self):
        self.driver.find.element(By.XPATH, Locators.logo).click()