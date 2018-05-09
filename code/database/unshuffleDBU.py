#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.log import warn as printf
import os
from random import randrange as rand

if isinstance(__builtins__,dict) and 'raw_input' in __builtins__:
	scanf = raw_input
elif hasattr(__builtins__,'raw_input'):
	scanf = raw_input
else:
	scanf = input

COLSIZ = 10
FIELDS = ('login','userid','projid')
RDBMSs = {'s':'sqlite','m':'mysql','g':'gadfly'}
DBNAME = 'pydb'
DBUSER = 'root'
DBPASS = 'root'
DBHOST = '127.0.0.1'
DBPORT = 3306
DB_EXC = None
NAMELEN = 16

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)

def setup():
	return RDBMSs[scanf('''
	Choose a database system:
	
	(M)ySQL
	(G)adfly
	(S)QLite
	
	Enter choice:''').strip().lower()[0]]


def connect(db,DBNAME):
	global DB_EXC
	dbDir = '{}_{}'.format(db,DBNAME)
	if db == 'sqlite':
		try:
			import sqlite3
		except ImportError:
			try:
				from pysqlite2 import dbapi2 as sqlite3
			except ImportError:
				return None
		DB_EXC = sqlite3
		if not os.path.isdir(dbDir):
			os.mkdir(dbDir)
		cxn = sqlite3.connect(os.path.join(dbDir,DBNAME))

	elif db == 'mysql':
		try:
			import pymysql
			pymysql.install_as_MySQLdb()
			import MySQLdb
			import pymysql.err as DB_EXC
			try:
				cxn = MySQLdb.connect(host=DBHOST,port=DBPORT,user=DBUSER,passwd=DBPASS,db=DBNAME,charset='utf8')
			except DB_EXC.OperationalError:
				try:
					cxn = MySQLdb.connect(user=DBUSER)
					cxn.query('CREATE DATABASE %s' % DBNAME)
					cxn.commit()
					cxn.close()
					cxn = MySQLdb.connect(db=DBNAME)
				except DB_EXC.OperationalError:
					return None
		except ImportError:
			try:
				import mysql.connector
				import mysql.connector.errors as DB_EXC

				try:
					cxn = mysql.connector.Connect(**{
						'database':DBNAME,
						'user':DBUSER
					})
				except DB_EXC.InterfaceError:
					return None
			except ImportError:
				return None
	elif db == 'gadfly':
		try:
			from gadfly import gadfly
			DB_EXC = gadfly
		except ImportError:
			return None

		try:
			cxn = gadfly(DBNAME,dbDir)
		except IOError:
			cxn = gadfly()
			if not os.path.isdir(dbDir):
				os.mkdir(dbDir)
			cxn.startup(DBNAME,dbDir)

	else:
		return None
	return cxn

def create(cur):
	try:
		cur.execute('''
			CREATE TABLE IF NOT EXISTS users(
				login VARCHAR(%d),
				userid INTEGER,
				PROJID INTEGER)
		''' % NAMELEN)
	except DB_EXC.OperationalError as e:
		drop(cur)
		create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
	('arron',8321),('angela',7603),('dave',730446),
	('davina',7902),('elliot',7911),('ernie',7410)
)

def randName():
	pick = set(NAMES)
	while pick:
		yield pick.pop()

def insert(cur,db):
	if db == 'sqlite':
		cur.executemany("INSERT INTO users VALUES(?,?,?)",
		[(who,uid,rand(1,5)) for who,uid in randName()])
	elif db == 'gadfly':
		for who,uid in randName():
			cur.execute("INSERT INTO users VALUES(?,?,?)",(who,uid,rand(1,5)))
	elif db == 'mysql':
		cur.executemany("INSERT INTO users VALUES(%s,%s,%s)",[(who,uid,rand(1,5)) for who,uid in randName()])

getRC = lambda cur: cur.rowcount if hasattr(cur,'rowcount') else -1

def update(cur):
	fr = rand(1,5)
	to = rand(1,5)
	cur.execute("UPDATE users SET projid=%d WHERE projid=%d" % (to,fr))
	return fr,to,getRC(cur)

def delete(cur):
	rm = rand(1,5)
	cur.execute("DELETE FROM users where projid=%d" % rm)
	return rm,getRC(cur)

def dbDumb(cur):
	cur.execute('select * from users')
	printf('\n%s' % ''.join(map(cformat,FIELDS)))
	for data in cur.fetchall():
		printf(''.join(map(tformat,data)))

def main():
	db = setup()
	printf('*** Connect to %r database ' % db)
	cxn = connect(db,DBNAME)
	if not cxn:
		printf('Error:%r not support or unreachable, exit' % db)
		return
	cur = cxn.cursor()

	printf('\n*** Creating users table')
	create(cur)
	printf('\n*** Inserting names into table')
	insert(cur,db)
	dbDumb(cur)

	printf('\n*** Randomly moving folks')
	fr,to,num = update(cur)
	printf('\t(%d users moved) from (%d) to (%d)' % (num,fr,to))
	dbDumb(cur)

	printf('\n*** Randomly choosing group')
	rm,num = delete(cur)
	printf('\t(group #%d; %d user removed)' % (rm,num))
	dbDumb(cur)

	#printf('\n*** Dropping users table')
	#drop(cur)
	#printf('\n*** Close cxns')
	cur.close()
	cxn.commit()
	cxn.close()

if __name__ == '__main__':
    main()



