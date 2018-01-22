print("hello,world")
#name=input("please type your name:")
#print("your name is:",name)

print(13/3)
print(1.2e5)
print(1.2e-4)
print(1.2e-5)

print("I\'m \"OK\"!")
print("\\\n\t\\")
print(r'\\\n\t\\')
print('line1\nline2\nline3')
print('''line1
line2
line3''')
print(r'''hello,\n
world''')

print(True)
print(3<2)
print(2<3 and 3<2)
print(2<3 or 3<2)

print(15/3)
print(14/3)
print(14//3)
print(14%3)

n=123
f=456.789
s1='hello,world'
s2='hello,\'Adam\''
s3=r'hello,"Bard"'
s4=r'''hello,
Lisa!'''
s5='''hello,
Lisa.'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print("这是中文字符串")
print(ord('A'),ord('中'),chr(66),chr(25991))
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
