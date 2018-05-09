#!/usr/bin/env python

import math

print("Hello, World!")

i = 10
print(i)

print("这是测试")

# 判断语句

if i < 5 :
	print('Less than 5')
else:
	print('More than 5')

# 字符串操作

str = 'Helloworld'

print(str)
print(str[:])
print(str[2:])
print(str[:3])
print(str[2:5])

# 数组
arr = ['jhon','rain','love','python']

print(arr)
print(arr[:])
print(arr[1:])
print(arr[2:3])
print(arr * 2)

# 元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
print(tuple[:])
print(tuple[2:])

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
list[2] = 1000     # 列表中是合法应用
print(list)

#tuple[2] = 1000    # 元组中是非法应用


print(2**5)

print(32//4.0)
print(32//4)
print(36.0/4)


num = 5
if num == 3:            # 判断num的值
	print('boss')
elif num == 2:
	print('user')
elif num == 1:
	print('worker')
elif num < 0:           # 值小于零时输出
	print('error')
else:
	print('roadman')     # 条件均不成立时输出


numbers = [12,44,55,78,9,22]
even = []
odd = []
while len(numbers)>0 :
	number = numbers.pop();
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)
print(even)
print(odd)

# 循环语句
for letter in 'Python':  # 第一个实例
	print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
	print('当前水果 :', fruit)

print("Good bye!")

# 冒泡排序
arrays = [1,8,9,3,2,6,4]
for i in range(len(arrays)):
	for j in range(i+1):
		if arrays[i] < arrays[j]:
			arrays[i],arrays[j] = arrays[j],arrays[i]


print(math.sin(math.pi/2))


