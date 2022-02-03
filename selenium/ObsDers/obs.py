from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Obs:
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser  = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
    
    def open(self):
        self.browser.get('https://obs.mersin.edu.tr/')
        time.sleep(2)
        button1 = self.browser.find_element_by_xpath('//*[@id="lblGkmContent"]/div/div/div/a[2]')
        button1.click()
        time.sleep(2)
        kullanıcıAdi = self.browser.find_element_by_xpath('//*[@id="txtParamT01"]')
        sifre = self.browser.find_element_by_xpath('//*[@id="txtParamT02"]')
        button2 = self.browser.find_element_by_xpath('//*[@id="btnLogin"]')
        time.sleep(1)
        kullanıcıAdi.send_keys('19155082')
        sifre.send_keys('12345678')
        time.sleep(3)
        button2.click()
        time.sleep(2)
        dersDonem = self.browser.find_element_by_xpath('//*[@id="proMenu"]/li[3]/a')
        dersDonem.click()
        time.sleep(2)
        dersKayit = self.browser.find_element_by_xpath('//*[@id="proMenu"]/li[3]/ul/li[1]/a')
        dersKayit.click()
        time.sleep(2)



    def checkLesson(self):
        dersKayit = self.browser.find_element_by_xpath('//*[@id="proMenu"]/li[3]/ul/li[1]/a')
        time.sleep(2)
        self.browser.switch_to_window( self.browser.window_handles[1])
        time.sleep(1)
        kontrol = self.browser.find_element_by_xpath('//*[@id="btnKontrolEt"]')
        

        while(1):
            dersKayit.click()
            time.sleep(2)
            kontrol.click()
            time.sleep(2)
            tamam = self.browser.find_element_by_xpath('/html/body/div/div/div[3]/button[1]')
            tamam.click()
            time.sleep(2)




obs = Obs()
obs.open()
obs.checkLesson()

