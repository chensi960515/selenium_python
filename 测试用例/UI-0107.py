from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

from 测试用例.config.addInfo import ADD_CUSTOMER, ADD_MEDICION
from 测试用例.config.indexConfig import INDEX_INFO

from 测试用例.config.libConfig import CHECK_POINT

wd = INDEX_INFO()

# 在系统中添加3种药品
ADD_MEDICION('青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装')
sleep(1)
ADD_MEDICION('青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装')
sleep(1)
ADD_MEDICION('青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装')
sleep(1)
# 在系统中添加3个客户
ADD_CUSTOMER('南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501')
sleep(1)
ADD_CUSTOMER('南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502')
sleep(1)
ADD_CUSTOMER('南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503')

wd.find_element_by_css_selector('.sidebar-menu a[href="#/orders"]').click()
wd.find_element_by_css_selector(
    'div .add-one-area button[type="button"]').click()

name = wd.find_element_by_css_selector('.add-one-area .form-control')
name.send_keys('南京中医院订单001')

# 客户选择 南京中医院2    药品选择 青霉素盒装1    数量填入 100盒
selectElements = wd.find_elements_by_css_selector('.add-one-area select')

Select(selectElements[0]).select_by_visible_text('南京中医院2')
Select(selectElements[1]).select_by_visible_text('青霉素盒装1')

inputs = wd.find_elements_by_css_selector('.add-one-area input')
inputs[2].send_keys('100')

wd.find_elements_by_css_selector('.add-one-area button')[0].click()
sleep(1)

orders = wd.find_elements_by_css_selector(
    '.search-result-item')[0].find_elements_by_tag_name('span')

medicion = wd.find_element_by_css_selector(
    '.search-result-item .search-result-item-field p')

order_list = [order_info.text for order_info in orders]
order_list.append(medicion.text)
del order_list[2:4]
print(order_list)

CHECK_POINT('订单信息是否和输入的一致', order_list == [
    '订单：',
    '南京中医院订单001',
    '客户：',
    '南京中医院2',
    '药品：',
    '青霉素盒装1 * 100'])

wd.quit()
