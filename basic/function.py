#call function
n1=255
n2=1000
print("255的十六进制表示为:",hex(n1))
print("1000的十六进制表示为:",hex(n2))

#define function
def test(x):
    if x > 5:
        print('x > 5 :',x)
        return "hello"
    else:
        print('x < 5 :',x)
        return "godbye"
print(test(100))

#test('A')

#isinstance函数进行数据类型检查
def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError('bad operand type')
    if x >= 0:
        print("正是一个正数：",x)
        return "正数绝对值为："+str(x)
    else:
        print("这是一个复数：",x)
        return "负数绝对值为："+str(-x)
print(my_abs(-1))
