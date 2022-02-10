# -*- coding: utf-8 -*-

print("hello world")
print("猿人学", "python", "爬虫")
print("猿人学", "python", "爬虫", sep=";")

# print("猿人学", "python", "爬虫", end="")

# a=input("请输入:")
# print(a)

name, age = "猿人学 ", 3
print(name, age)
# id用来输出变量的地址
print(id(name))

myAge = 30
print(myAge/2)
print(myAge//2)
print(float(myAge))

myMoney = 100.23633
myMoney1 = round(myMoney, 2)  #四舍五入
print(myMoney1)

myage = 3
myage = pow(3, 2)
print(myage)

myage = 30
myage = str(30)
print(myage)
print(type(myage))

name = "猿人学"
name = '猿人学'
name = """猿人学"""
name = '''猿人学'''

mynum = "abcdefghi"
first = mynum[0]
print("first=", first)

name = "%s 30岁" % name
print(name)

myMoney = '我的工资是%.4f' % 300.345754
print(myMoney)

myMoney = 300.345754
myMoney = "我的工资是:{}".format(myMoney)
print(myMoney)

#3.6以后写法
money = 200.34
myMoney = f"22我的工资是:{money}"
print(myMoney)

myName = '猿人学'
print(len(myName))

myName = "abcdefgh"
print("find:", myName.find("h"))
print("find:", myName.index("h"))
# print("find:", myName.index("z"))

# startwith,endwith,upper,lower,islower

url = "http.www.baidu.com"
print(url.replace("http", "https"))

# strip(), strip(k)
#zfill
#isdigit



