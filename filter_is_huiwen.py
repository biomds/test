#!/usr/bin/python 
# -*- coding:utf-8 -*-
'''
利用filter函数获得从0到输入数字范围内的回文数
'''
def is_huiwen(n):
	n=str(n)
	rev_n = ''.join(reversed(n))
	if rev_n == n:
		return n
	else:
		return False
print"找出从0到输入的数之间的回文数"
n=input("Enter a number：")
result=list(filter(is_huiwen,range(n)))
print "找出的回文数是:",result

