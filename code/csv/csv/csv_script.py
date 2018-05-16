#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def csv_writer():
	"""写入csv文件"""
	headers = ["编号", "课程", "讲师"]
	rows = [
		(1, "python", "jery"),
		(2, "C#", "jery"),
		(3, "java", "jery"),
		(4, "Django", "jery"),
		(5, ".Net", "jery"),
	]

	with open('my_course.csv', 'w', encoding='utf-8', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(headers)
		writer.writerows(rows)


def csv_writer_dict():
	"""写入csv文件"""
	headers = ["ID", "Title", "Org"]
	rows = [
		{"ID":1, "Title":"python", "Org":"org"},
		{"ID":2, "Title":"C#", "Org":"org"},
		{"ID":3, "Title":"java", "Org":"org"},
		{"ID":4, "Title":"Django", "Org":"org"},
		{"ID":5, "Title":".Net", "Org":"org"},
	]

	with open('my_course_dict.csv', 'w', encoding='utf-8', newline='') as f:
		writer = csv.DictWriter(f,headers)
		writer.writeheader()
		writer.writerows(rows)


if __name__ == '__main__':
	csv_writer_dict()
