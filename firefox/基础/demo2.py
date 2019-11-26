from selenium import webdriver
from time import sleep

wd = webdriver.Firefox()
wd.get('file:///E:/soft/WebTest/demo.html')
wd.implicitly_wait(5)

wd.find_element_by_id('user').send_keys('自动化测试')
sleep(2)
wd.find_element_by_id('user').clear()
sleep(1)
wd.find_element_by_id('user').send_keys('我不想不会')

wd.find_element_by_tag_name('textarea').send_keys('111111111111111')

wd.find_element_by_xpath('//a[contains(@href,"baidu")]').click()