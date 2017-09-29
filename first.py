#coding=utf-8

# 注释  for循环
#for i in range(1,5):
#    for j in range(1,5):
#        for k in range(1,5):
#            if( i != k ) and (i != j) and (j != k):
#                print i,j,k

#列表
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
#更新列表
list1[2] = 2001;
print "New value available at index 2 : "
print list1[2];

del list1 [2]
print list1

#插入一个元素
#list1.insert(2,'hello')
#print list1

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#list2.extend(list1)
#print list2
#检查元素是否存在于列表中
print '7' in list2

#比较两个列表的元素
print cmp(list2,list1)
