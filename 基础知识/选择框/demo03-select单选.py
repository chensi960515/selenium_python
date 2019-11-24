from selenium import webdriver
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/test2.html')
wd.implicitly_wait(5)


select = Select(wd.find_element_by_id('ss_single'))
select.select_by_value('小雷老师')
