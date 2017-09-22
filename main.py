#coding=utf-8
#import first.py


#print "你好吗"
#print "hello python"

"""变量定义的规则：
    变量名只能是 字母、数字或下划线的任意组合
    变量名的第一个字符不能是数字
    以下关键字不能声明为变量名
    ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield'] """
name1 = "wupeiqi"
print name1
name  = "China"
print(name)
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
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))


months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum

