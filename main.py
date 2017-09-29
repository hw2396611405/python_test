#coding=utf-8
#import first.py #列表
#元组
import unit.py

"""变量定义的规则：
    变量名只能是 字母、数字或下划线的任意组合
    变量名的第一个字符不能是数字
    以下关键字不能声明为变量名
    ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield'] """
name1 = "wupeiqi"
print name1
name  = "China"
print(name)


#i = 2
#while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#        if not(i%j): break
#        j = j + 1
#      if (j > i/j) :print i, " 是素数"
#      i = i + 1
#
#print "Good bye!"

#i = int(raw_input('ssss:'))
##i = 600000
#arr = [1000000,600000,400000,200000,100000,0]
#rat = [0.01,0.015,0.03,0.05,0.075,0.1]
#r = 0
#for idx in range(0,6):
#    if i>arr[idx]:
#        r+=(i-arr[idx])*rat[idx]
#        print (i-arr[idx])*rat[idx]
#        i=arr[idx]
#print r


#year = int(input('year:\n'))
#month = int(input('month:\n'))
#day = int(input('day:\n'))


#months = (0,31,59,90,120,151,181,212,243,273,304,334)
#if 0 < month <= 12:
#    sum = months[month - 1]
#else:
#    print 'data error'
#sum += day
#leap = 0
#if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#    leap = 1
#if (leap == 1) and (month > 2):
#    sum += 1
#print 'it is the %dth day.' % sum

#x="a"
#y="b"
## 换行输出
#print x
#print y
#
#print '---------'
## 不换行输出
#print x,
#print y,
#
## 不换行输出
#print x,y


#count = 0
#while count < 5:
#    print count, " is  less than 5"
#    count = count + 1
#else:
#    print count, " is not less than 5"

#while 语句
#import random
#while 1:
#    s = int(random.randint(1, 3))
#    if s == 1:
#        ind = "石头"
#    elif s == 2:
#        ind = "剪子"
#    elif s == 3:
#        ind = "布"
#    m = raw_input('输入 石头、剪子、布,输入"end"结束游戏:')
#    blist = ['石头', "剪子", "布"]
#    if (m not in blist) and (m != 'end'):
#        print "输入错误，请重新输入！"
#    elif (m not in blist) and (m == 'end'):
#        print "\n游戏退出中..."
#        break
#    elif m == ind :
#        print "电脑出了： " + ind + "，平局！"
#    elif (m == '石头' and ind =='剪子') or (m == '剪子' and ind =='布') or (m == '布' and ind =='石头'):
#        print "电脑出了： " + ind +"，你赢了！"
#    elif (m == '石头' and ind =='布') or (m == '剪子' and ind =='石头') or (m == '布' and ind =='剪子'):
#        print "电脑出了： " + ind +"，你输了！"

#i = 1
#while i :
#    j = 1
#    while j:
#        print j ,"*", i ," = " , i * j , '  ',
#        if i == j :
#            break
#
#        j += 1
#        if j >= 10:
#            break
#    print "\n"
#    i += 1
#    if i >= 10:
#        break  #注意缩进

