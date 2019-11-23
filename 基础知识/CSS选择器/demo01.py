from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('http://f.python3.vip/webauto/sample1.html')

wd.find_element_by_css_selector('#searchtext').send_keys('您好')

#wd.close()