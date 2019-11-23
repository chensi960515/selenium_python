from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/sample1a.html')

#wd.implicitly_wait(1)

elements = wd.find_elements_by_css_selector('#t1>span,#t1>p')
#下面的任何数据都取不出来 div 不能和id一起使用吗?
#elements = wd.find_elements_by_css_selector('div #t1>span,div #t1>p')
for element in elements:
    print(element.text)

wd.quit()