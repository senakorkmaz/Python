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
        usernameBoxPath ='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
        passwordBoxPath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
        singInButtonPath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'
        
        usernameBox = self.browser.find_element_by_xpath(usernameBoxPath)
        passwordBox = self.browser.find_element_by_xpath(passwordBoxPath)
        singInButton = self.browser.find_element_by_xpath(singInButtonPath)
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

    def findTweet(self):
        results = []
        scrollHeight = 'return document.documentElement.scrollHeight'
        tweetPath = '//div[@class="css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]'

        last_height = self.browser.execute_script(scrollHeight)
        list = self.browser.find_elements_by_xpath(tweetPath)
        time.sleep(2)
        for i in list:
            results.append(i.text)

        while True:
            self.browser.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')
            time.sleep(2)
            
            list = self.browser.find_elements_by_xpath(tweetPath)
            time.sleep(2)
            for i in list:
                results.append(i.text)
            new_heigth = self.browser.execute_script(scrollHeight)
            time.sleep(1)
            if last_height == new_heigth:
                break
            last_height = new_heigth
        
        self.writeFile(results)

    def writeFile(self,list):
        count = 1
        with open('tweet.txt','a',encoding="utf-8") as file:
            for i in list:
                file.write(f"{count}-{i}\n")
                count+=1
