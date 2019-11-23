from selenium import webdriver
from time import sleep

wd= webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/sample1.html')

wd.implicitly_wait(5)

elements = wd.find_elements_by_css_selector('.animal')
for element in elements:
    print(element.text)

wd.close()