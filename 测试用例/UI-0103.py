from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_tag_name('button').click()

wd.find_element_by_class_name('sidebar-menu').find_elements_by_tag_name('span')[1].click()

wd.find_element_by_class_name('container-fluid').find_element_by_class_name('glyphicon-plus').click()


inputs = wd.find_element_by_class_name('add-one-area').find_elements_by_class_name('form-control')

#添加数据
# 输入药名
inputs[0].send_keys('倍他乐克片')
# 输入编号
inputs[1].send_keys('SLD998877')
# 输入客户姓名
inputs[2].send_keys('沙美特罗替卡松气雾剂 适应症为舒利迭 适用于对哮喘进行常规治疗的患者的联合用药')

wd.find_elements_by_class_name('btn-xs')[0].click()

sleep(1)

fields = wd.find_elements_by_class_name('search-result-item')[0].find_elements_by_tag_name('span')[1:6:2]
texts = [field.text for field in fields]
print(texts)

# 预期内容为
expected = [
'倍他乐克片',
'SLD998877',
'沙美特罗替卡松气雾剂 适应症为舒利迭 适用于对哮喘进行常规治疗的患者的联合用药'
]

print(f'\n** 检查点 **  客户信息和添加内容一致 ')

if texts == expected:
    print('---->  通过')
else:
    print('---->   !! 不通过!!')
    exit(1)

wd.quit()
