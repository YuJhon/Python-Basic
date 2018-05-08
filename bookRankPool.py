#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib import request
from urllib.request import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNS = {
	'0132269937':'Core Python Programming',
	'0132356139':'Python Web Development with Django',
	'0137143419':'Python Fundamentals'
}

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

def getRanking(isbn):
	req = request.Request('%s%s' % (AMZN, isbn), {}, head)
	with uopen(req) as page:
		return str(REGEX.findall(page.read().decode('utf-8'))[0])

def _main():
	print('At ',ctime(),'On Amazon...')
	with ThreadPoolExecutor(3) as executor:
		for isbn,ranking in zip(ISBNS,executor.map(getRanking,ISBNS)):
			print('- %r ranked %s' % (ISBNS[isbn], ranking))
		print('All Done At:',ctime())


if __name__ == '__main__':
	_main()