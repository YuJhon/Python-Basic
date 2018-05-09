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

import urllib.request
import random

url = 'http://http://www.whatismyip.com.tw/'
print("添加多个ip地址（IP:端口号）,多个IP地址使用分号隔开！")
iplist = input('请开始输入：').split(sep=";")
while True:
	ip = random.choice(iplist)
	proxy_support = urllib.request.ProxyHandler({'http': ip})
	opener = urllib.request.build_opener(proxy_support)
	#opener.add_handlers = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')]
	urllib.request.install_opener(opener)
	try:
		print('正在尝试使用 %s 访问 。。。' % ip)
		response = urllib.request.urlopen(url)
		#html = response.read().decode('utf-8')
	except urllib.error.URLError:
		print("访问出错")
	else:
		print('访问成功')
	if input("请问是否要再来一次（Y/N）：") == 'N':
		break;
#223.199.173.246:808;221.226.20.158:8080;219.136.172.174:9797