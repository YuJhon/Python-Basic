#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def json_basic():
	data = {
		"ID": 1,
		"课程": "python 简介",
		"机构": "aaa"
	}

	json_str = json.dumps(data)
	print(json_str)
	json_str = json.loads(json_str)
	print(json_str)

def json_writer_file():
	"""写json到文档"""
	data = {
		"ID": 1,
		"课程": "python 简介",
		"机构": "aaa"
	}
	with open('data.json','w',encoding='utf-8') as f:
		json.dump(data,f)

def json_read_file():
	"""读取json文件"""
	with open('data.json','r',encoding='utf-8') as f:
		data = json.load(f)
		print(data)

if __name__ == '__main__':
	json_read_file()
