from selenium import webdriver
from time import sleep

from 基础知识.CSS选择器.config.lib import CHECK_POINT

wd = webdriver.Chrome()
wd.get('http://127.0.0.1/mgr/sign.html')

wd.implicitly_wait(1)

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')

wd.find_element_by_tag_name('button').click()

wd.find_element_by_class_name('sidebar-menu').find_elements_by_tag_name('span')[1].click()


wd.find_element_by_css_selector('.container-fluid .add-one-area .btn-outlined').click()

inputs = wd.find_elements_by_css_selector('.add-one-area .form-control')

# 输入 药品名称
inputs[0].send_keys('青霉素盒装1')
# 输入 编号
inputs[1].send_keys('YP-32342349')
# 输入 描述
inputs[2].send_keys('青霉素注射液，每支15ml，20支装')

wd.find_elements_by_class_name('btn-xs')[0].click()

# 等待1秒
sleep(1)

items = wd.find_elements_by_css_selector('div.search-result-item span')[:6]

texts = [item.text for item in items]
print(texts)

expected=['药品：', '青霉素盒装1', '编号：', 'YP-32342349', '描述：', '青霉素注射液，每支15ml，20支装']

CHECK_POINT('药品信息和添加内容一致', texts == expected)

wd.quit()