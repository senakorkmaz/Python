from githubUserInfo import username,password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        
    def singIn(self):
        self.browser.get('https://github.com/login')
        time.sleep(2)
        usernameBox = self.browser.find_element_by_xpath('//*[@id="login_field"]')
        passwordBox = self.browser.find_element_by_xpath('//*[@id="password"]')
        singInButton = self.browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
        usernameBox.send_keys(self.username)
        passwordBox.send_keys(self.password)
        time.sleep(1)
        singInButton.click()

    def getFollowers(self):
        #self.browser.get(f'https://github.com/{self.username}?tab=followers')
        self.browser.get('https://github.com/aryashah2k?tab=followers')
        time.sleep(2)
        
        items = self.browser.find_elements_by_css_selector('.d-table.table-fixed')
        for i in items:
            print(i.find_element_by_css_selector('.Link-secondary.pl-1').text)

github =Github(username,password)
github.singIn()
github.getFollowers()