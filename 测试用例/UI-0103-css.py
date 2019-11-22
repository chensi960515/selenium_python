from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.implicitly_wait(1)

wd.get('http://127.0.0.1/mgr/sign.html')

# 根据id选择元素,并添加值
wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')

# 根据标签名查找元素
wd.find_element_by_tag_name('button').click()

# 找到所有的菜单
menus = wd.find_elements_by_css_selector('.sidebar-menu span')

# 选择第一个span元素,客户为第一个

menus[0].click()

wd.find_element_by_css_selector('.glyphicon-plus').click()

# 找到输入框
inputs = wd.find_elements_by_css_selector('.add-one-area .form-control')

# 根据输入框输入不同的值
# 输入客户姓名
inputs[0].send_keys('南京中医院')
# 输入联系电话
inputs[1].send_keys('2551867858')
# 输入客户姓名
inputs[2].send_keys('江苏省-南京市-秦淮区-汉中路-16栋504')

buttons = wd.find_elements_by_css_selector('.add-one-area .btn-outlined')
buttons[0].click()

sleep(1)

# 找到第一个客户,点击编辑
wd.find_elements_by_css_selector('.search-result-item .btn-outlined')[0].click()

# 进行改名的操作,首先先清除之前的内容
inputs = wd.find_elements_by_css_selector('.search-result-item .form-control')
inputs[0].clear()
inputs[0].send_keys('北京市中医院')

# 更改完成,点击确定按钮,打印出更改之后的内容,并且退出浏览器窗口
wd.find_elements_by_css_selector('.search-result-item .btn-outlined')[0].click()

# 获取之前添加的信息并打印出来
first_div = wd.find_elements_by_css_selector('.search-result-item')
spans = first_div[0].find_elements_by_css_selector('span')

spans_list_key = []
spans_list_value = []

for span in spans[0:5:2]:
    spans_list_key.append(span.text)
for span in spans[1:6:2]:
    spans_list_value.append(span.text)

# zip方法是将两个列表转换为字典
dict_costomer = dict(zip(spans_list_key, spans_list_value))
print(type(dict_costomer))
# 遍历字典 有错误,zip和items不能用
for k, v in dict_costomer.items():
    print(k + v)

wd.quit()
