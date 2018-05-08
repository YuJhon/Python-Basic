#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiangy19'
__mtime__ = '2018/5/5'
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
import time

class TimeCounter:
	# 重写方法
	def __init__(self):
		self.unit = ['年','月','日','时','分','秒']
		self.prompt = "未开始计时"
		self.lasted = []
		self.begin = 0
		self.end = 0
	# 重写方法

	def __repr__(self):
		return self.prompt

	# 计算运行时间
	def _calc(self):
		self.lasted = []
		self.prompt = "总共运行了"
		for index in range(6):
			self.lasted.append(self.end[index] - self.begin[index] )
			if(self.lasted[index]):
				self.prompt += str(self.lasted[index]) + self.unit[index]
		self.begin = 0
		self.end = 0
	# 开始计时
	def start(self):
		self.begin = time.localtime()
		self.prompt = "提示：先调用stop()结束计时"
		print("计时开始")
	# 结束计时
	def stop(self):
		if not self.begin:
			print("提示：请先调用start()开始计时")
		else:
			self.end = time.localtime()
			self._calc()
			print("计时结束！")
	# 重写add方法
	def __add__(self, other):
		prompt = "总共运行了"
		result = []
		for index in range(6):
			result.append(self.lasted[index] + other.lasted[index])
			if result[index]:
				prompt += (str(result[index])+self.unit[index])
		return prompt;


	def test(self):
		print('测试方法');

if __name__ == '__main__':
	TimeCounter().test()