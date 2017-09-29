# -*- coding: UTF-8 -*-
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup3 = tup1 +tup2
print tup3

tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup;

#复制
tup4 = ('Hi!',) * 4
print tup4

#将列表转换为元组
list1 = ['physics', 'chemistry', 1997, 2000];
tup5 = tuple(list1)
print tup5

#计算元组元素个数
leight = len(tup5)
print leight

print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;
