#!/usr/bin/python 
# -*- coding -utf-8 -*-
'''
��ѧ����ѧϰ�ɼ��ֱ��������ͳɼ�����
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

## Method1
#������������
def by_name(t):
    return t[0].lower()
#���շ�������
def by_score(t):
    return t[1]
L2 = sorted(L,key=by_name)
L3 = sorted(L,key=by_score)
print("������������Ľ����%s" % L2)
print("���շ�������Ľ����%s" % L3)

## Method2
#������������
L4 = sorted(L,key=lambda x:x[0].lower())
#���շ�������
L5 = sorted(L,key=lambda x:x[1])
print("������������Ľ����: %s" % L4)
print("���շ�������Ľ����: %s" % L5)