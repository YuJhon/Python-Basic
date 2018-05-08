#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import ctime
import threading

class MyThread(threading.Thread):

	def __init__(self,func,args,name=''):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name

	def getResult(self):
		return self.res

	def run(self):
		print("start ",self.name,'at:',ctime())
		self.res = self.func(*self.args)
		print(self.name,"finished at:",ctime())
#