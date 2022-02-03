from selenium import webdriver
import time

driver = webdriver.Chrome()


# url = 'http://github.com'
# driver.get(url)

# time.sleep(2)
# driver.maximize_window()
# driver.save_screenshot('github.com-homepage.png')
# print(driver.title)
# time.sleep(2)

newUrl = 'http://github.com/sadikturan'
driver.get(newUrl)

driver.implicitly_wait(2)

driver.maximize_window()
print(driver.title)
if "sadikturan" in driver.title:
    driver.save_screenshot('github-sadikturan.png')

driver.implicitly_wait(2)
driver.back()
driver.implicitly_wait(2)
driver.forward()
#driver.close()