#list列表
#创建一个list
classmates = ['simba','bill','rose']
print(len(classmates))
print('classmates:',classmates)
#按照索引号查找元素
print('classmates[0]:',classmates[0])
print('classmates[1]:',classmates[1])
print('classmates[2]:',classmates[2])
print('classmates[-1]:',classmates[-1])
print('classmates[-2]:',classmates[-2])
print('classmates[-3]:',classmates[-3])
#末尾添加一个元素
classmates.append('hello')
print(classmates)
#指定索引位置插入元素
classmates.insert(2,'tom')
print(classmates)
#删除末尾元素
classmates.pop()
print(classmates)
#删除指定索引位置的元素
classmates.pop(0)
print(classmates)
#将指定索引位置的元素进行替换
classmates[0]='simba'
print(classmates)

#混合数组
L=['simba',100,True]
num=L[1]+200
print(num)

#二维数组
s=['simba','joy',['tom','jerry'],'java','php']
print(len(s))
print(s)
print(s[2])
print(s[2][0])

#tuple元组
t=('python','php','java','c++')
print(t)
print(t[0],t[2])

#tuple单元素需加‘，’，否则会视为单括号
t=('hello')
print(len(t))
t=('hello',)
print(len(t))

#可变的tuple
t=('a','b',['A','B'])
print(t)
t[2][0]='Y'
t[2][1]='Z'
print(t)

#练习
L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
    ]
#打印Apple
print(L[0][0])
#打印Python
print(L[1][1])
#打印Lisa
print(L[2][2])

#可变tuple查看内存地址
list=['A','B']
print('id(list):',id(list))
t=('a','b',list)
print('id(t[2]):',id(t[2]))
list=['X','Y']
print('id(list):',id(list))
print('id(t[2]):',id(t[2]))
print('t[2]:',t[2])
print('list:',list)
