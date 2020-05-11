from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class FaceBot:
    def __init__(self,username,passwrd):
        self.username   = username
        self.password   = passwrd
        self.url        = 'https://facebook.com'
        self.driver     = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get('{}'.format(self.url))
        sleep(2)
        driver.find_element_by_name('email').send_keys(self.username)
        driver.find_element_by_name('pass').send_keys(self.password + Keys.RETURN)
        sleep(4)

    def Events(self):
        sleep(1)
        driver = self.driver
        driver.get('{}/events'.format(self.url))
    
    def Birthdays(self):
        sleep(1)
        driver = self.driver
        driver.find_element_by_class_name('gs1a9yip ow4ym5g4 auili1gw rq0escxv j83agx80 cbu4d94t buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 tgvbjcpo hpfvmrgz rz4wbd8a a8nywdso l9j0dhe7 du4w35lb rj1gh0hx f10w8fjw pybr56ya').click()

      

    def findfriend(self,person):
#            """
#            After login find a person on Facebook
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
#            Send a like on Facebook picture(s)
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
#            Send a comment on Facebook picture(s)
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
        driver.find_element_by_class_name('').click()
        sleep(0.5)
        i = 1
        if amount > 1:
            while (i <= amount):
                driver.find_element_by_class_name('').click()
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


# face = FaceBot(username, passwrd)
# face.login()            # Login works
# face.Events()           # Direct to Events
# face.Birthdays()        # Working on - Go to Birthdays and post Happy Bday
 
if __name__ == '__main__':

    usr = str(input('What is your Facebook username? (case sensitive): '))
    paswrd = getpass.getpass(prompt='What is your Facebook password (case sensitive): ', stream=None)

    face = FaceBot(usr,paswrd)
    face.login() 
    face.Events()

