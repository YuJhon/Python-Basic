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
import re
from bs4 import BeautifulSoup

def main():
	url = "http://baike.baidu.com/view/284853.htm"
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,"html.parser")

	for each in soup.find_all(href=re.compile("view")):
		print(each.text,"->","".join(["http://baike.baidu.com",each["href"]]))

if __name__ == '__main__':
	main()