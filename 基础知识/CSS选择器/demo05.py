from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/sample1b.html')

#wd.implicitly_wait(1)

elements = wd.find_elements_by_css_selector('span:nth-child(2)')
for element in elements:
    print(element.text)

wd.quit()