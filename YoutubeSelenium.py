from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path='C:/users/junna/chromedriver.exe')
url = 'https://blackboard.angelo.edu'
driver.get(url)
#창 크게 열기
driver.maximize_window()

#Agree & Continue
driver.find_element_by_id('agree_button').click()

#Type in id
id = driver.find_element_by_id('user_id')
id.send_keys('jpark43')
pw = driver.find_element_by_id('password')
pw.send_keys('qkrwnsgk7#')

#Click login
driver.find_element_by_id('entry-login').click()

#Wait for 2 seconds
time.sleep(2)

#Click CS3304
driver.find_element_by_xpath('//*[@id="_4_1termCourses_noterm"]/ul/li[1]/a').click()

#Click collaborate session tab
driver.find_element_by_xpath('//*[@id="paletteItem:_786592_1"]/a/span').click()