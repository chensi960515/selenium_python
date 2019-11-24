from selenium import webdriver
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/test2.html')
wd.implicitly_wait(5)

selects = Select(wd.find_element_by_id('ss_multi'))

selects.deselect_all()

selects.select_by_value('小雷老师')
selects.select_by_value('小江老师')