#!/usr/bin/env python
# -*- coding: utf-8 -*-

from atexit import register
from random import randrange
from threading import Thread, BoundedSemaphore, Lock
from time import ctime, sleep

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)


def refill():
	lock.acquire()
	print("Refilling candy ...")
	try:
		candytray.release()
	except ValueError:
		print('full,skipping')
	else:
		print('OK')
	lock.release()


def buy():
	lock.acquire()
	print("Buying candy...")
	if candytray.acquire(False):
		print('OK')
	else:
		print('empty,skipping')
	lock.release()


def producer(loops):
	for i in range(loops):
		refill()
		sleep(randrange(3))


def consumer(loops):
	for i in range(loops):
		buy()
		sleep(randrange(3))


def _main():
	print("start at :", ctime())
	nloops = randrange(2, 6)
	print('HTE CANDY MACHINE （full with %d bars）!')
	Thread(target=consumer, args=(randrange(nloops, nloops + MAX + 2),)).start()
	Thread(target=producer,args=(nloops,)).start()

@register
def _atexit():
	print('All Done At:', ctime())


if __name__ == '__main__':
	_main()
