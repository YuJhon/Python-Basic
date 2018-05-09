#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.log import warn as printf
from os.path import dirname
from random import randrange as rand
from sqlalchemy import Column,Integer,String,create_engine,exc,orm
from sqlalchemy.ext.declarative import declarative_base

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

NAMES = (
	('arron',8321),('angela',7603),('dave',730446),
	('davina',7902),('elliot',7911),('ernie',7410)
)

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)


def setup():
	return RDBMSs[scanf('''
	Choose a database system:

	(M)ySQL
	(S)QLite

	Enter choice:''').strip().lower()[0]]

def randName():
	pick = set(NAMES)
	while pick:
		yield pick.pop()

DSNs = {
	'mysql':'mysql+mysqldb://%s:%s@%s/%s' % (DBUSER,DBPASS,DBHOST,DBNAME),
	'sqlite':'sqlite:///:memory:'
}

Base = declarative_base()
class Users(Base):
	__tablename__ = 'users'
	login = Column(String(NAMELEN))
	userid = Column(Integer,primary_key=True)
	projid = Column(Integer)

	def __str__(self):
		return ''.join(map(tformat,(self.login,self.userid,self.projid)))

class SQLAlchemyTest(object):
	def __init__(self,dsn):
		try:
			eng = create_engine(dsn)
		except ImportError:
			raise RuntimeError()
		try:
			eng.connect()
		except exc.OperationalError:
			eng = create_engine(dirname(dsn))
			eng.execute('CREATE DATABASE %s' % DBNAME).close()
			eng = create_engine(dsn)

		Session = orm.sessionmaker(bind=eng)
		self.ses = Session()
		self.users = Users.__table__
		self.eng = self.users.metadata.bind = eng

	def insert(self):
		self.ses.add_all(
			Users(login=who,userid=userid,projid=rand(1,5)) for who,userid in randName()
		)
		self.ses.commit()

	def update(self):
		fr = rand(1,5)
		to = rand(1,5)
		i = -1
		users = self.ses.query(Users).filter_by(projid=fr).all()
		for i,user in enumerate(users):
			user.projid = to
		self.ses.commit()
		return fr,to,i+1

	def delete(self):
		rm = rand(1,5)
		i = -1
		users = self.ses.query(Users).filter_by(projid=rm).all()
		for i,user in enumerate(users):
			self.ses.delete(user)
		self.ses.commit()
		return rm,i+1

	def dbDump(self):
		printf('\n%s' % ''.join(map(cformat,FIELDS)))
		users = self.ses.query(Users).all()
		for user in users:
			printf(user)
		self.ses.commit()

	def __getattr__(self,attr):
		return getattr(self.users,attr)

	def finish(self):
		self.ses.connection().close()


def main():
	printf('*** Connect to %r database' % DBNAME)
	db = setup()
	if db not in DSNs:
		printf('\nERROR: %r not support ,exit' % db)
		return

	try:
		orm = SQLAlchemyTest(DSNs[db])
	except RuntimeError:
		printf('\n Error: %r not supported,exit' % db)
		return

	printf('\n*** Create users table (drop old one if appl.)')
	orm.drop(checkfirst=True)
	orm.create()

	printf('\n*** Insert names into table')
	orm.insert()
	orm.dbDump()

	printf("\n*** Move users to a random group")
	fr,to,num = orm.update()
	printf('\t(%d users moved) from (%d) to (%d)' % (num,fr,to))
	orm.dbDump()

	printf('\n*** Randomly delete grop')
	rm,num = orm.delete()
	printf('\t(group #%d; %d users removed)' % (rm, num))
	orm.dbDump()

	#printf('\n*** Drop users table')
	#orm.drop()
	#printf('\n*** Close cxns')
	#orm.finish()

if __name__ == '__main__':
    main()