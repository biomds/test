#!/usr/bin/python
# -*- coding:utf-8 -*-
# 字符串的find方法有返回值（如果没找到，则返回-1），但index方法不一定有返回值（如果没找到，则报错）
from functools import  reduce
dig = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

# Method 1
## Method1_1
def str2float_1_1(s):
    def cha2num(s):
        return dig[s]
    return reduce(lambda x,y:x*10+y,map(cha2num,s.replace(".","")))
s=input("Enter a string number: ")
if s.find(".") != -1:
    result = str2float_1_1(s)/pow(10,(len(s)-s.find(".")-1))
    print("str2float_1_1(\'%s\')="%s,result)
else:
    result = str2float_1_1(s)
    print("str2float_1_1(\'%s\')="%s,result)
## Method1.2
def str2float_1_2(s):
    def cha2num(s):
        return dig[s]
    if s.find(".") == -1:
        return reduce(lambda x,y:x*10+y,map(cha2num,s))
    else:
        return reduce(lambda x,y:x*10+y,map(cha2num,s.replace(".","")))/pow(10,(len(s)-s.find(".")-1))

print("str2float_1_2(\'%s\')="%s,str2float_1_2(s))


# Method 2
def str2float_2(s):
    def cha2num(s):
        return dig[s]
    n = s.find(".")
    if n == -1:
        return reduce(lambda x,y:x*10+y,map(cha2num,s))
    else:
        s1 = s[:n]
        s2 = s[n+1:]
        return reduce(lambda x,y:x*10+y,map(cha2num,s1))+reduce(lambda x,y:x*10+y,map(cha2num,s2))/10**len(s2)
print("str2float_2(\'%s\')="%s,str2float_2(s))


