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
import urllib.parse
import json

content = input("请输入需要翻译的内容：")
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = {}
data['doctype'] = 'json'
data['from'] = 'zh-CHS'
data['to'] = 'en'
data['smartresult'] = 'dict'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'
data['i']=content
data['version']='2.1'
data['client']='fanyideskweb'
data['salt']='1525492222253'
data['sign']='a3dfaa865240fcc3e5850c09ff12917b'
head={}
head['Referer']='http://fanyi.youdao.com/'
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
print(html)
#target = json.load(html)
#print('翻译结果为：%s' % (target['translateResult'][0][0]['tgt']))