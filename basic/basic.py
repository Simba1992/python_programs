#name=input("Hello,Please enter your name:")
#print("Hello, "+name+" now enter your num")
num1=input("First num:")
num2=input("Second num:")
print('字符串：num1 + num2 =',num1+num2)
print('数字：int(num1) * int(num2) =',int(num1)*int(num2))

test=1
print(test==1)
print(test==2)
print(test==1 or test==2)
print(test==1 and test==2)
def fabFunc(n):
    if n<2:
        print('------------>1',n)
        return -1
    if n==2 or n==3:
        print('------------>2',n)
        return 1
    else:
        print('------------>3',n)
        return fabFunc(n-2)+fabFunc(n-3)

d=fabFunc(5)
print(d)

