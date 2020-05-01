
from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,passwrd):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(5)

InstaBot()