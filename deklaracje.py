from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import Locators

class Testy():

    def test1(self):

        driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        driver.maximize_window()
        driver.get('https://ncplusgo.pl')
        driver.find_element(By.XPATH, Locators.logo).click()

    def test2(self):
        driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        driver.maximize_window()
        driver.get('https://ncplusgo.pl')
        driver.find_element(By.XPATH, Locators.terazwtv).click()

run = Testy()
run.test1()