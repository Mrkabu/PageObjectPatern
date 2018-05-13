from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import Locators

class Testy():

    def __init__(self):
        self.driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://ncplusgo.pl')

    def test1(self):

        self.driver.find_element(By.XPATH, Locators.logo).click()
        self.driver.find_element(By.XPATH, Locators.login).send_keys('login@login.pl')
        self.driver.find_element(By.XPATH, Locators.password).send_keys('pass')
        self.driver.find_element(By.XPATH, Locators.buttonzaloguj).click()

    def test2(self):

        self.driver.find_element(By.XPATH, Locators.terazwtv).click()

run = Testy()
run.test1()