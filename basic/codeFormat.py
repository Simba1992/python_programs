#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("hello world!")
#encode函数将unicode字符串编码为指定格式
print("hello".encode('ascii'))
print("hello".encode('utf-8'))
print("hello".encode('gbk'))
#print("国家".encode('ascii'))
print("国家".encode('utf-8'))
print("国家".encode('gbk'))
#decode函数将特定格式的字符串编码解码为unicode
print(b'\xe5\x9b\xbd\xe5\xae\xb6'.decode('utf-8'))
print(b'\xb9\xfa\xbc\xd2'.decode('gbk'))

a='中文'
print(a.encode('utf-8'))
print(len('中国人民'))
print(len(b'\xe5\x9b\xbd\xe5\xae\xb6'))

print('hello %s,your score is %d.\\%%'%('simba',98))
print('%2d-%02d' % (3,1))
print('%2d' % (31))
print('%.2f' % 3.1415926)

s1=72
s2=85
r=(s2-s1)/s1*100
print('score rate is %.1f' % r)

s='Python-中文'
print(s)
b=s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
