#dict键-值（key-value）存储
d={'simba':95,'tom':80,'jerry':60}
print("dict d is:",d)
print(d['tom'])
d['java']=1
print(d)
print(d.get('java'))
print(d.get('php'))
print(d.get('php',-1))
d.pop('java')
print(d)

#set一组key的集合，可以看成数学意义上的无序和无重复元素的集合
s1=set([1,2,3,4,5])
s2=set([4,5,6,7,8])
print(s1 & s2)
print(s1 | s2)

s=set((1,2,3))
print(s)
#(1,[2,3])是可变对象，不能作key
#s=set((1,[2,3]))
#print(s)
#(1,2,3)是不可变对象，可以作value
s={'a':(1,2,3)}
print(s)
print(s['a'])
#(1,[2,3])是可变对象，可以作value
s={'a':(1,[2,3])}
print(s)
print(s['a'])
#(1,[2,3])是可变对象，不能作key
#s={(1,[2,3]):a}
#print(s)
