#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('library.db')

sql = "select * from LinkMan"
c = conn.cursor()
# result = c.execute(sql)
# for row in result:
# 	print(row)


c.execute(sql)
lst = c.fetchall()
for row in lst:
	print(row)