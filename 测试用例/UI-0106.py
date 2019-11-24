from selenium import webdriver
from time import sleep

from 基础知识.CSS选择器.config.lib import CHECK_POINT

wd = webdriver.Chrome()
wd.get('http://127.0.0.1/mgr/sign.html')
wd.implicitly_wait(5)

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_tag_name('button').click()

old_windows = wd.current_window_handle
wd.find_element_by_css_selector('.main-footer .pull-right').click()

for wnd in wd.window_handles:
    wd.switch_to.window(wnd)
    if '白月黑羽教学网' in wd.title:
        break

wd.maximize_window()

items = wd.find_elements_by_css_selector('#site-nav li')
titles = [item.text for item in items]
print(titles)

CHECK_POINT('白月黑羽官网菜单是否和预期一致',titles == [
                'Python基础',
                'Python进阶',
                'Web开发',
                '自动化和性能测试',
                'Linux和MySQL',
                '练习作业',
                '常见问题',
                '好文分享'
             ])
wd.close()
wd.switch_to.window(old_windows)

wd.find_element_by_css_selector('.navbar-custom-menu .user-menu').click()
wd.find_element_by_css_selector('.user-footer .pull-right').click()

sleep(2)

CHECK_POINT('检查是否进入登陆页面','/mgr/sign.html' in wd.current_url)

wd.quit()