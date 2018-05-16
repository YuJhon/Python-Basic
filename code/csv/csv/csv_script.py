#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def csv_writer():
	"""写入csv文件"""
	headers = ["编号","课程","讲师"]
	rows = [
		(1,"python","jery"),
		(2,"C#","jery"),
		(3,"java","jery"),
		(4,"Django","jery"),
		(5,".Net","jery"),
	]

	with open('my_course.csv','w',encoding='utf-8',newline='') as f:
		writer = csv.writer(f)
		writer.writerow(headers)
		writer.writerows(rows)


if __name__ == '__main__':
    csv_writer()