from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url = 'http://github.com'
driver.get(url)

searchInput = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
#searchInput = driver.find_element_by_name('q')
time.sleep(4)
searchInput.send_keys('python')
time.sleep(4)
searchInput.send_keys(Keys.ENTER)
time.sleep(4)
result = driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/a')

for element in result:
    print(element.text)
driver.close()