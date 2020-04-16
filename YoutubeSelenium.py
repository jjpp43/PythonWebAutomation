from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path='C:/users/junna/chromedriver.exe')
url = 'https://blackboard.angelo.edu'
driver.get(url)
#Maximize window
driver.maximize_window()

#Click Agree & Continue button
driver.find_element_by_id('agree_button').click()

#Type in my id
id = driver.find_element_by_id('user_id')
id.send_keys('myID')  #I have hidden my id for security purposes
#Type in my password
pw = driver.find_element_by_id('password')
pw.send_keys('myPassword')  #I have hidden my password for security purposes

#Click login
driver.find_element_by_id('entry-login').click()

#Wait for 2 seconds
time.sleep(2)

#Click my CS3304 course
driver.find_element_by_xpath('//*[@id="_4_1termCourses_noterm"]/ul/li[1]/a').click()

#Click collaborate session tab, and now I am in my online class :)
driver.find_element_by_xpath('//*[@id="paletteItem:_786592_1"]/a/span').click()
