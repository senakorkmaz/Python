
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser  = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)

        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get('https://twitter.com/login')
        time.sleep(2)

        usernameBox = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        passwordBox = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        singInButton = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')

        usernameBox.send_keys(self.username)
        passwordBox.send_keys(self.password)
        time.sleep(1)

        singInButton.click()
        time.sleep(2)

    def searchWithHashtag(self,hashtag):
        searchInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
        searchInput.send_keys(hashtag)
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        
        last_height = self.browser.execute_script('return document.documentElement.scrollHeight')
        while True:
            self.browser.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')
            time.sleep(2)
            new_heigth = self.browser.execute_script('return document.documentElement.scrollHeight')
            if last_height == new_heigth:
                break
            last_height = new_heigth
        

        list = self.browser.find_elements_by_xpath('//div[@class="css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
        time.sleep(10)
        for item in list:
            print(item.text)
            print('********')

