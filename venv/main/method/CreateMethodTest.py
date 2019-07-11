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


# 默认参数  默认参数必须放到后面 默认参数必须指向不可变当对象 看下面错误例子 eg

def add(a, b=1, c=1):
    return a + b


print(add(1, 2, 3))


def eg(list=[]):
    list.append(1)
    return list


# 这里第二次打印当时候就出错了 因为python在定义函数当就指定好了默认值 即内存当地址 可以使用none来实现
print(eg())
print(eg())


def eg1(list=None):
    if list is None:
        list = []
    list.append(1)
    return list

print(eg1())
print(eg1())