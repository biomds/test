#!/usr/bin/python 
# -*- coding -utf-8 -*-
'''
对学生的学习成绩分别按照姓名和成绩排序
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

## Method1
#按照名称排序
def by_name(t):
    return t[0].lower()
#按照分数排序
def by_score(t):
    return t[1]
L2 = sorted(L,key=by_name)
L3 = sorted(L,key=by_score)
print("按照名称排序的结果是%s" % L2)
print("按照分数排序的结果是%s" % L3)

## Method2
#按照名称排序
L4 = sorted(L,key=lambda x:x[0].lower())
#按照分数排序
L5 = sorted(L,key=lambda x:x[1])
print("按照名称排序的结果是: %s" % L4)
print("按照分数排序的结果是: %s" % L5)