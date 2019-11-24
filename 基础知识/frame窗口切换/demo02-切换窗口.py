from selenium import webdriver
from time import sleep

wd= webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/sample3.html')
#wd.implicitly_wait(5)

#保存老窗口,便于后面的窗口转换
old_windows = wd.current_window_handle

link = wd.find_element_by_tag_name('a')
link.click()

for handle in wd.window_handles:
    #先切换到该循环的窗口
    wd.switch_to.window(handle)
    #如果此次判断中,获得的窗口标题栏字符串,判断是不是需要操作的那个窗口,如果是则跳出循环
    #跳出循环之后,wd对象指向的也是此次循环中得到的新的窗口
    if 'bing' in wd.title:
        break

#经过循环之后,wd指向的窗口对象已经改变
wd.find_element_by_id('sb_form_q').send_keys('白夜黑羽\n')
elements = wd.find_element_by_id('b_results')
item = elements.find_elements_by_css_selector('.b_algo')[0]
print(item.text)

wd.switch_to.window(old_windows)

wd.find_element_by_id('outerbutton').click()

print(wd.title)