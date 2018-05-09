#!/usr/bin/env python
# -*- coding: utf-8 -*-

from atexit import register
from re import compile
from threading import Thread
from time import ctime
import urllib

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
	req = urllib.request.Request('%s%s' % (AMZN,isbn), {}, head)
	page =urllib.request.urlopen(req)
	data = page.read().decode('utf-8')
	page.close()
	#print(data)
	return REGEX.findall(data)[0]

def _showRanking(isbn):
	print('- %r ranked %s' % (ISBNS[isbn],getRanking(isbn)))

def _main():
	print('At ',ctime(),'on Amazon...')
	for isbn in ISBNS:
		#_showRanking(isbn)
		Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
	print('All Done At:',ctime())

if __name__ == '__main__':
	_main()

