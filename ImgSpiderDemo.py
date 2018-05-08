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
import  requests
import urllib.request
import re
import os

def openUrl(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
	page = urllib.request.urlopen(req)
	html = page.read().decode('gbk')
	return html

def getImg(html):
	p = r'<img alt*.*?src="([^"]*\.jpg)".*?>'
	imgList = re.findall(p,html)
	try:
		os.mkdir("NewPic")
	except FileExistsError:
		pass
	os.chdir("NewPic")

	for each in imgList:
		filename = each.split('/')[-1]
		# 如果不设置头部信息，则会被拦截掉
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
		res = requests.get(each,headers=headers)
		with open('picture_'+filename, 'wb') as f:
		 	f.write(res.content)

if __name__ == '__main__':
    url = "http://www.meizitu.com/a//5555.html"
    getImg(openUrl(url))
