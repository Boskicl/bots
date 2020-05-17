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
        driver.find_element_by_css_selector('#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div.rq0escxv.l9j0dhe7.tkr6xdv7.j83agx80.cbu4d94t.d2edcug0.pfnyh3mw.dp1hu0rb.rek2kq2y.o36gj0jk > div > div.q5bimw55.ofs802cu.dkue75c7.mb9wzai9.o8kakjsu.rpm2j7zs.k7i0oixp.gvuykj2m.j83agx80.cbu4d94t.ni8dbmo4.eg9m0zos.buofh1pr.l56l04vs.r57mb794.l9j0dhe7.kh7kg01d.c3g1iek1.k4xni2cv > div.a8s20v7p.k5wvi7nf.buofh1pr.pfnyh3mw.l9j0dhe7.du4w35lb > div.aov4n071 > div:nth-child(3) > a > div.ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.nnctdnn4.hpfvmrgz.qt6c0cv9.jb3vyjys.l9j0dhe7.du4w35lb.bp9cbjyn.btwxx1t3.dflh9lhu.scb9dxdr').click()
        # Working on getting number of birthdays present.... can select birthdays for now
        print(driver.find_elements_by_css_selector('#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.rj1gh0hx.buofh1pr.g5gj957u.hpfvmrgz.dp1hu0rb > div > div > div > div > div:nth-child(1) > div > div > div > div.dati1w0a.qt6c0cv9.hv4rvrfc.jb3vyjys.b20td4e0'))


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

    #usr = str(input('What is your Facebook username? (case sensitive): '))
    #paswrd = getpass.getpass(prompt='What is your Facebook password (case sensitive): ', stream=None)
    face = FaceBot(usr,paswrd)
    face.login() 
    face.Events()
    face.Birthdays()

