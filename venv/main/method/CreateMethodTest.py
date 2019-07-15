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


# 可变参数
def kbch(*numbles):
    for n in numbles:
        print(n)


# kbch(1, 2, 3, 4, 5, 6)
# 如何把集合变成可变参数
nums = [1, 3, 5, 7, 9]


# kbch(*nums)


# 关键字参数

def gjz(name, age, **data):
    print('name{0},age:{1} data:{2}'.format(name, age, data))


gjz('tian', 'xiao', a='a', b='b')

# 关键字参数只能填city或者sex
def gjz2(name,age,*,city,sex):
    print('data:'+ city+"  sex:"+sex)

gjz2('tian',1,city='beijing',sex='nan')

# 方法参数申明顺序   必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
