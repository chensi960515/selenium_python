from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

from 测试用例.config.addInfo import ADD_CUSTOMER, ADD_MEDICION,ADD_ORDER
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
ADD_CUSTOMER('安徽中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501')
sleep(1)
ADD_CUSTOMER('南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502')
sleep(1)
ADD_CUSTOMER('南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503')

order_list = ADD_ORDER('订单xxx','安徽中医院1','青霉素盒装1','100')

CHECK_POINT('订单信息是否和输入的一致',order_list == [
        '订单：',
        '南京中医院订单001',
        '客户：',
        '南京中医院2',
        '药品：',
        '青霉素盒装1 * 100'])

wd.quit()