#for函数
names = ("java","php","python","C++")
for name in names:
    print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print("sum from 1 to 10 is:",sum)


#range函数生成整数序列
print("range(5):",range(5))
print("list(range(5))：",list(range(5)))
print("range(5)[2]:",range(5)[2])
print("list(range(5))[2]:",list(range(5))[2])

L=range(101)
sum=0
for x in L:
    sum = sum + x
print("sum from 1 to 101 is:",sum)

#while函数
sum=0
n=99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L=['Bart','Lisa','Adam']
#while版本
x=0
while x<len(L):
    print('Hello,%s!' % L[x])
    x = x + 1

#for版本    
for a in L:
    print('Hello,%s!' % a)

#break语句：提前退出循环
n=1
while n <= 100:
    if n > 10:
        print('Ready to end')
        break
    print(n)
    n = n + 1
print('End')

#continue语句：跳过当次循环
n=0
while n < 10:
    n=n+1
    if n%2==0:
        continue
    print(n)

