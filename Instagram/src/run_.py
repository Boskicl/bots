from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaBot:
    def __init__(self,username,passwrd):
        self.username   = username
        self.password   = passwrd
        self.url        = 'https://instagram.com'
        self.driver     = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get('{}/accounts/login/'.format(self.url))
        sleep(3)
        driver.find_element_by_name('username').send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        sleep(4)
        driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        sleep(3)

    def profile(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.username)).click()
        sleep(3)

    def findfollower(self,person):
        driver = self.driver
        driver.get('{}/{}/'.format(self.url,person))

    def like(self,amount):
        driver = self.driver
        driver.find_element_by_class_name('eLAPa').click()
        sleep(2)
        try:
            driver.find_element_by_class_name('fr66n').click()
        except Exception as e:
            sleep(1)


insta = InstaBot('username', 'password')
insta.login()
insta.findfollower('ljubeb')
insta.like(1)
