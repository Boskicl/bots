from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
        sleep(2)
        driver.find_element_by_name('username').send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        sleep(3)
        driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        sleep(2)

    def profile(self):
#            """
#            Log into a Instagram profile
#            ...
#
#            Attributes
#            ----------
#            self : 
#                class of Webdriver
#                [will passthrough username,password]
#
#            """
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.username)).click()
        sleep(3)

    def findfollower(self,person):
#            """
#            After login find a person on Instgram
#            ...
#
#            Attributes
#            ----------
#            self : 
#                class of Webdriver
#            person : str
#                username of person whose account you want to visit
#
#            """
        driver = self.driver
        driver.get('{}/{}/'.format(self.url,person))

    def like(self,amount):
#            """
#            Send a like on Instagram picture(s)
#            ...
#
#            Attributes
#            ----------
#            self : 
#                class of Webdriver
#            amount : int
#                the amount of pictures to like
#
#            """
        driver = self.driver
        driver.find_element_by_class_name('eLAPa').click()
        sleep(0.5)
        i = 1
        if amount > 1:
            while (i <= amount):
                driver.find_element_by_class_name('fr66n').click()
                sleep(0.2)
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                sleep(1)
                i += 1
        else: 
            sleep(1)
            driver.find_element_by_class_name('fr66n').click()

    def comment(self,text,amount):
#            """
#            Send a comment on Instagram picture(s)
#            ...
#
#            Attributes
#            ----------
#            self : 
#                class of Webdriver
#            text : str
#                the text you want to comment (same for each picture)
#            amount : int
#                the amount of pictures to comment on
#
#            """
        driver = self.driver
        driver.find_element_by_class_name('eLAPa').click()
        sleep(0.5)
        i = 1
        if amount > 1:
            while (i <= amount):
                driver.find_element_by_class_name('Ypffh').click()
                act = ActionChains(driver)
                sleep(0.5)
                act.send_keys(text + Keys.RETURN)
                act.perform()
                sleep(0.2)
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                sleep(1)
                i += 1
        else:
            sleep(1)
            driver.find_element_by_class_name('Ypffh').click()
            act = ActionChains(driver)
            sleep(0.5)
            act.send_keys(text + Keys.RETURN)
            act.perform()

    def like_comment_multi(self,text,amount):
#            """
#            Send a like and comment on Instagram picture(s)
#            ...
#
#            Attributes
#            ----------
#            self : 
#                class of Webdriver
#            text : str
#                the text you want to comment (same for each picture)
#            amount : int
#                the amount of pictures to comment on
#
#            """
        driver = self.driver
        driver.find_element_by_class_name('eLAPa').click()
        sleep(0.5)
        i = 1
        while (i <= amount):
                driver.find_element_by_class_name('fr66n').click()
                sleep(0.2)
                driver.find_element_by_class_name('Ypffh').click()
                act = ActionChains(driver)
                sleep(0.5)
                act.send_keys(text + Keys.RETURN)
                act.perform()
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                sleep(1)
                i += 1
amount = 2 # Amount of Likes/comments to give

insta = InstaBot('usrn', 'pswrd')
insta.login()
insta.findfollower('ljubeb')
#insta.like(amount) 
#insta.comment('Nice picture!',amount) 
insta.like_comment_multi('Nice picture!',amount) 
