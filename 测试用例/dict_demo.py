spans_list_key = ['客户名：', '联系电话：', '地址：']
spans_list_value = ['北京市中医院', '2551867858', '江苏省-南京市-秦淮区-汉中路-16栋504']
dict_costomer = {}

dict_costomer = dict(zip(spans_list_key,spans_list_value))
print(type(dict_costomer))

for k,v in dict_costomer.items():
    print(k + v)
