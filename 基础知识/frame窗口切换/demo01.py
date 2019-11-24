from selenium import webdriver
from time import sleep

wd= webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/sample2.html')
#wd.implicitly_wait(5)

wd.switch_to.frame('frame1')

elements = wd.find_elements_by_class_name('plant')
for element in elements:
    print(element.text)

wd.switch_to.default_content()

wd.find_element_by_id('outerbutton').click()