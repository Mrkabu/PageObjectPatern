from selenium.webdriver.common.by import By

class Locators(object):

    logo = (By.XPATH, '/html/body/header/div/div/div/div/div/div/a/img')
    terazwtv = (By.XPATH, '/html/body/header/div/div/div/div/div/nav/a[1]')
    programtv = (By.XPATH, '/html/body/header/div/div/div/div/div/nav/a[2]')
    zaloguj = (By.XPATH, '/html/body/header/div/div/div/div/nav/ul/li[3]/a')
