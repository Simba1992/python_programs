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

