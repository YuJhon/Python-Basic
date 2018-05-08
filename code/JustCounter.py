#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiangy19'
__mtime__ = '2018/5/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

class JustCounter:
	__secretCount = 0
	publicCount = 1

	def count(self):
		self.__secretCount += 2
		self.publicCount += 10
		print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()

print(counter.publicCount)

#print(counter.__secretCount)
print(counter._JustCounter__secretCount)