#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
利用python的内置函数filter查找一组数当中的质数
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_prime(n):
	if n > 1:
		for i in range(2,n):
			if n % i == 0:
				return False
				break
		else:
			return n
	else:
		return False
print"找出从0到输入的数之间的质数"
n=input("Enter a number：")
n=int(n)
result=list(filter(is_prime,range(n)))
print "找出的质数是:",result

