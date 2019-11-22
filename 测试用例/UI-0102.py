from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_tag_name('button').click()

tree = wd.find_element_by_class_name('sidebar-menu')
elements = tree.find_elements_by_tag_name('span')
elements[0].click()

wd.find_element_by_class_name('glyphicon-plus').click()

inputs = wd.find_element_by_class_name('add-one-area').find_elements_by_class_name('form-control')

# 输入客户姓名
inputs[0].send_keys('南京中医院')
# 输入联系电话
inputs[1].send_keys('2551867858')
# 输入客户姓名
inputs[2].send_keys('江苏省-南京市-秦淮区-汉中路-16栋504')

wd.find_element_by_class_name('add-one-area').find_elements_by_class_name('btn-xs')[0].click()

sleep(2)

item = wd.find_elements_by_class_name('search-result-item')[0]
fields = item.find_elements_by_tag_name('span')[1:6:2]
texts = [field.text for field in fields]
print(texts)


# 预期内容为
expected = [
'南京中医院',
'2551867858',
'江苏省-南京市-秦淮区-汉中路-16栋504'
]

print(f'\n** 检查点 **  客户信息和添加内容一致 ')

if texts == expected:
    print('---->  通过')
else:
    print('---->   !! 不通过!!')
    exit(1)

wd.quit()
