from selenium import webdriver
import unittest

class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\Python\Drivery\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://ncplusgo.pl')