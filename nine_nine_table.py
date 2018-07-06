#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
打印九九乘法表
'''
for i in range(1,10):
	for j in range(1,10):
		num = i*j
		print("%3d" %num,end=" ")
	print()
