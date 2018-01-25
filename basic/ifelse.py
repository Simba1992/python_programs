#-*- coding: utf-8 -*-
age=int(input("Please input your age:"))
if age>=18:
    print("Your age is %d, you are adult." % age)
elif age>=6:
    print("Your age is %d, you are teenager." % age)
else:
    print("Your age is %d, you are kid." % age)

birth=int(input("birth:"))
if birth < 2000:
    print("00前")
else:
    print("00后")

#height=1.75
#weight=80.5
height=float(input("Input your height:"))
print(height)
weight=float(input("Input your weight:"))
print(weight)
BMI=weight/(height**2)
print("height*height:",height*height)
print("height**2:",height**2)
print("BMI :",BMI)
if BMI < 18.5:
    print("体重过轻")
elif BMI >= 18.5 and BMI < 25:
    print("体重正常")
elif BMI >= 25 and BMI < 28:
    print("体重过重")
elif BMI >=28 and BMI < 32:
    print("体重肥胖")
else:
    print("严重肥胖")
