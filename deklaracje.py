#  from selenium.webdriver.common.by import By
from selenium import webdriver

class Deklaracje(object):

    def __init__(self):

        self.driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://ncplusgo.pl')

    def zaloguj(self, name = '//*[@id="top"]/div/div/div/div/nav/ul/li[3]/a/img'):

        z = self.driver.find_element_by_xpath(name).click()
        #  t = By.XPATH, '/html/body/header/div/div/div/div/div/nav/a[1]'  #  teraz w tv
        #  p = By.XPATH, '/html/body/header/div/div/div/div/div/nav/a[2]'  #  program tv
        #  z = By.XPATH, '//*[@id="top"]/div/div/div/div/nav/ul/li[4]/a/img'  #  zaloguj


run = Deklaracje()
run.zaloguj()