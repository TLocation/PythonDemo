print('100+200:', 100 + 200)

a = 100
if a > 100:
    print(a)
else:
    print(-a)

print("start String")

print("start length:", len('str'))

# list
list = ['a', 'b', 'c']
print('list length:{0} index 0:{1}'.format(len(list), list[0]))
# 获取最后一项的
print(list[-1])
# 追加
list.append(12)
list.insert(1, 13)
list.sort()
print(list)
# 删除 不加参数删除末尾的 加了参数 删除对应索引的
list.pop()
# 替换元素
list[0] = "than"
print(list)
# 不可变的集合
finallist = (3, 2)
print(finallist)
# 集合参考网址 https://www.liaoxuefeng.com/wiki/1016959663602400/1017092876846880


# if语句
# ifArgs = input()
# if len(ifArgs)<3:
#     print('输出的数小于3')
# elif len(ifArgs)==3:
#     print("输入的数等于3")
# else:
#     print('输出的数大于3')

#     for循环
# for it in list:
#     print(it)

# 0到4
for it in range(5):
    print(it)

# 集合dict相当于map
tempDict = {'name': 'tianxiaolong', 'age': '26'}
tempDict['sex'] = '男'
print(tempDict['name'])
print(tempDict['sex'])
# 如果没有会报错 可以使用
print('id' in tempDict)
print(tempDict.get('id', 'no have id'))

# set 和java一样 不可重复
setTemp = set([1,2,3])
print(setTemp)
# 添加
setTemp.add(5)
print(setTemp)
# 使用set做交集 并集 地址： https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448
set1 = set([1, 3, 5])
set2 = set([5, 6, 7])
print(set1 & set2)
print(set1 | set2)



