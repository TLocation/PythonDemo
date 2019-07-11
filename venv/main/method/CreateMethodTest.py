# 定义函数练习 下面是引入包 引入math包
import math


def myAbs(x):
    if x > 0:
        return x
    else:
        return abs(x)


# pass代表还没想好怎么写 可以用于任何语句
def test():
    pass


# print(myAbs(-1))


# 定义参数的方法检查

def testTryMethod(x):
    # 如果参数不是int类型 或者float类型
    if not isinstance(x, (int, float)):
        raise TypeError("必须是int或者float")
    # 此函数不做任何事 只是检测参数类型
    pass


# 函数返回多个值

def getName():
    return "田晓龙", '张超'
