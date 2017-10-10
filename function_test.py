#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    函数规则
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
    """


# 定义函数
def printme( str ):
    "打印任何传入的字符串"
    print str;
    return;

# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");

#传入不可变对象实例
#def ChangeInt( a ):
#    a = 10
#
#b = 2
#ChangeInt(b)
#print b  # 结果是 2

#可写函数说明
def printme( str ):
    "打印任何传入的字符串"
    print str;
    return;

##调用printme函数
#printme("str");
##调用printme函数
#printme( str = "My string");

#可写函数说明  关键字参数
def printinfo( name, age ):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

#调用printinfo函数
#printinfo( age=50, name="miki" );

#可写函数说明   缺省参数
def printinfo( name, age = 23 ):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

#调用printinfo函数
printinfo( age=50, name="miki" );
printinfo( name="miki" );

# 不定长参数 可写函数说明
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
      print var
    return;

# 调用printinfo 函数
#printinfo( 10 );
#printinfo( 70, 60, 50 );

"""
    使用 lambda 来创建匿名函数。
    lambda只是一个表达式，函数体比def简单很多。
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
    """
# 匿名函数   可写函数说明
#终端测试
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
#print "相加后的值为 : ", sum( 10, 20 )
#print "相加后的值为 : ", sum( 20, 20 )

# return 语句 可写函数说明
def sum( arg1, arg2 ):
    # 返回2个参数的和."
    total = arg1 + arg2
    print "函数内 : ", total
    return total;

# 调用sum函数
total = sum( 10, 20 );

"""
    全局变量和局部变量
    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
    """

total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    return total;

#调用sum函数
total1 = sum( 10, 20 );
print "函数返回值测试:" ,total1
print "函数外是全局变量 : ", total


"""
    1、global---将变量定义为全局变量。可以通过定义为全局变量，实现在函数内部改变变量值。
    2、一个global语句可以同时定义多个变量，如 global x, y, z。
    这样全局函数可以作用于函数内
    """
globvar = 0

def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1

def print_globvar():
    print(globvar)     # 没有使用 global

set_globvar_to_one()
print  globvar        # 输出 1
print_globvar()       # 输出 1，函数内的 globvar 已经是全局变量

def funx(x):
    def funy(y):
        return x * y
    return funy    #return funy返回的是一个对象，可理解为funx是funy的一个对象

#print funx(7)(8)

