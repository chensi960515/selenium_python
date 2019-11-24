#将用例检查点封装为函数

def CHECK_POINT(desc,conditionRet):
    print(f'\n** 检查点 **  {desc} ')

    if conditionRet:
        print('---->  通过')
    else:
        print('---->   !! 不通过!!')
        exit(1)