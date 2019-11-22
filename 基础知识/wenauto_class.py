from selenium import webdriver
wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/sample1.html')

#选择所有的动物
# elements = wd.find_element_by_class_name('animal')
#
# for element in elements:
#     print(element.text)

#选择所有的tag名为 div的元素
# elements = wd.find_elements_by_tag_name('div')
#
# for element in elements:
#     print(element.text)

#限制 选择元素的范围是 id 为 container 元素的内部
element = wd.find_element_by_id('container')
spans = element.find_elements_by_tag_name('span')
for span in spans:
    print(span.text)


wd.quit()