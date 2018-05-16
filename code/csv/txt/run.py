#!/usr/bin/env python
# -*- coding: utf-8 -*-

def txt_write():
	"""写文件"""
	with open('data.txt', 'w', encoding='utf-8') as f:
		f.write('JhonRain\n');
		lines = [
			'地址：深圳市\n',
			'QQ:704351844\n',
			'网址：http://www.jhonrain.org'
		]
		f.writelines(lines)


def txt_read():
	"""读文件"""
	with open('data.txt', encoding='utf-8') as f:
		for line in f:
			print(line, end='')


if __name__ == '__main__':
	txt_read()
