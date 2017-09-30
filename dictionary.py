#coding=utf-8
#字典是另一种可变容器模型，且可存储任意类型对象。
#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print dict['Alice']

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry 添加元素


print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];

#删除字典元素  能删除单一的元素也能清空字典
del dict['Name']
#清空字典
dict.clear()
print dict
# 删除字典
del dict

