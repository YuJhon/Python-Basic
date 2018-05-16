#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CSV文件的读取"""
import csv
from collections import namedtuple


def csv_read():
	"""csv基本读取"""
	with open('housedata.csv', encoding="utf-8") as f:
		reader = csv.reader(f)
		headers = next(reader)

		print(headers)

		for row in reader:
			print(row)


def csv_read_by_namedtuple():
	"""读取csv并且用namedtuple映射列名"""
	with open('housedata.csv', encoding="utf-8") as f:
		reader = csv.reader(f)
		headers = next(reader)

		Row = namedtuple('Row', headers)

		for r in reader:
			row = Row(*r)
			print(row)


def csv_read_by_dict():
	"""读取csv到字典表"""
	with open('housedata.csv', encoding="utf-8") as f:
		reader = csv.DictReader(f)
		for row in reader:
			print(row)


if __name__ == '__main__':
	csv_read_by_dict()
