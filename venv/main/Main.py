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
list.insert(1,13)
print(list)
# 删除 不加参数删除末尾的 加了参数 删除对应索引的
list.pop()
# 替换元素
list[0] = "than"
print(list)
# 不可变的集合
finallist = (3,2)
print(finallist)
