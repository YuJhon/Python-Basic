#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

def xl_read():
	"""读取excel"""
	book = xlrd.open_workbook('product.xls')
	for sheet in book.sheets():
		print(sheet.name)


def xl_read_data():
	book = xlrd.open_workbook('product.xls')
	sheet = book.sheet_by_name('product')
	print("工作普：{}".format(sheet.name))
	print("数据函数：{}".format(sheet.nrows))
	print("产品数据")
	for i in range(sheet.nrows):
		print(sheet.row_values(i))  # 获取索引指定的数据含

if __name__ == '__main__':
	xl_read_data()