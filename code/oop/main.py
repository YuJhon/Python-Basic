#!/usr/bin/env python
# -*- coding: utf-8 -*-

def search_book(title):
	print('搜索包含关键字{}的图书'.format(title))


book = {
	'title': 'Python入门',
	'price': 55.99,
	'author': 'Perter',
	'search_book': search_book
}

print(book['title'])
print(book.get('price',0.0))
book.get('search_book')('python')
