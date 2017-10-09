#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
    Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
    时间间隔是以秒为单位的浮点小数。
    """

import time;  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print "本地时间为 :", localtime
