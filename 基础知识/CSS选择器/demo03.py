from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/sample1.html')

#wd.implicitly_wait(1)

#element = wd.find_element_by_css_selector('.footer1 .copyright')
#print(element.text)

#elements = wd.find_elements_by_css_selector('.plant, .animal')
# for element in elements:
#     print(element.text)

elements = wd.find_elements_by_css_selector('div,#BYTY')
for element in elements:
    print(element.text)


wd.quit()