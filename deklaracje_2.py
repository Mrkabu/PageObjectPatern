from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators import Locators

def test1():

    driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://ncplusgo.pl')
    driver.find_element(By.XPATH, Locators.logo).click()

def test2():
    driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://ncplusgo.pl')
    driver.find_element(By.XPATH, Locators.terazwtv).click()

test1()