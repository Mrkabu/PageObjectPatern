from Mainpage import Home
import unittest
from selenium import webdriver


class Firstsimplescript(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://ncplusgo.pl')

    def firsttest(self, driver):
        home = Home(driver)

        if home.getTerazwtv.is_displayed():
            print('Displayed')
            home.getTerazwtv.click()