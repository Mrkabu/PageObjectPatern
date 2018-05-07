from Locators import Locators #import z piku Locators.py gdzie definiujemy obiekty
from selenium.webdriver.common.by import By

class Home(object):

    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find.element(By.XPATH, Locators.logo)
        self.terazwtv = driver.find.element(By.XPATH, Locators.terazwtv)
        self.programtv = driver.find.element(By.XPATH, Locators.programtv)
        self.zaloguj = driver.find.element(By.XPATH, Locators.zaloguj)

    def getLogo(self):
        return self.logo

    def getTerazwtv(self):
        return self.terazwtv

    def getProgramtv(self):
        return self.programtv

    def getZaloguj(self):
        return self.zaloguj