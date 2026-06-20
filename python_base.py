# 变量
# x = 5
# print(x)
#
# x = "Hello"
# print(x)

# 数据类型: 数字 字符串 列表 元组 字典 集合

# 数字: 整数int 浮点数float 布尔bool
# x = 5
# print(x)
# print(type(x))
#
# y = 3.14
# print(y)
# print(type(y))
#
# a = True
# print(a)
# print(type(a))

# 类型转换
# b = int(3.14)
# print(b)
# print(type(b))
#
# c = float(5)
# print(c)
# print(type(c))
#
# d = bool(1)
# print(d)
# print(type(d))
#
# e = abs(-5)
# print(e)
#
# f = round(3.54)
# print(f)

# 字符串
# g = "Hello,World!"

# 切片
# 访问单个字符
# print(g[0])
# print(g[6])

# 获取字符串一部分
# print(g[0:5])
# print(g[6:])

# 负数索引切片
# print(g[-6:-1])

# step参数
# print(g[0:5:2])

# 省略参数

# 如何反转字符串?
# g = "Hello,World!"
# print(g[::-1])

# 字符串常用函数和方法

# len()函数
# length = len(g)
# print(length)

# lower()方法和upper()方法
# lower_case = g.lower()
# upper_case = g.upper()
# print(lower_case)
# print(upper_case)

# replace()方法
# new_g = g.replace("Hello","Hi")
# print(new_g)

# split()方法
# words = g.split(",")
# print(words)

# join()方法
# words = ['Hello', 'World!']
# h = " ".join(words)
# print(h)

# strip()方法
# h = "  Hello World! "
# trimmed_h = h.strip()
# print(trimmed_h)

# 元组
# 创建元组
# tuple1 = (1, 2, 3)

# 访问元组元素
# print(tuple1[0])
# print(tuple1[2])

# 元组不可变性
# tuple1[0] = 4

# 元组的切片
# tuple2 = (1, 2, 3, 4, 5)
# print(tuple2[1:4])

# 元组常用函数和方法

# count()方法
# tuple3 = (1, 2, 1, 3, 2, 4, 5)
# count = tuple3.count(1)
# print(count)

# index()方法
# index = tuple3.index(1)
# print(index)

# 获取重复元素所有索引
# indices = [i for i, value in enumerate(tuple3) if value == 1 ]
# print(indices)

# len()函数
# length = len(tuple3)
# print(length)

# sorted()函数
# sorted_tuple3 = sorted(tuple3)
# print(sorted_tuple3)

# 列表
# list1 = [1, 2, 3, 4, 5]

# 列表常用函数和方法

# len()函数
# length = len(list1)
# print(length)

# append()方法
# list1.append(6)
# print(list1)

# insert()方法
# list1.insert(3,8)
# print(list1)

# remove()方法
# list2 = [1, 3, 1, 4, 5]
# list2.remove(1)
# print(list2)

# pop()方法
# list3 = [1, 2, 3, 4]
# element = list3.pop(2)
# print(element)
# print(list3)

# sort()方法
# list4 = [3, 2, 1, 4, 5]
# list4.sort()
# print(list4)
#
# list4.sort(reverse=True)
# print(list4)

# sorted()函数
# list4 = [3, 2, 1, 4, 5]
# # sorted_list4 = sorted(list4)
# # print(sorted_list4)
# # print(list4)

# index()方法
# list2 = [1, 3, 1, 4, 5]
# index = list2.index(1)
# print(index)

# 字典
# person = {"name" : "jack", "age" : 18, "gender" : "man"}

# 字典常用函数和方法
# len()函数
# length = len(person)
# print(length)

# keys()方法
# keys = person.keys()
# print(keys)

# values()方法
# values = person.values()
# print(values)

# items()方法
# items = person.items()
# print(items)

# get()方法
# name = person.get("name")
# print(name)

# phone = person.get("phone", "N/A")
# print(phone)

# pop()方法
# age = person.pop("age")
# print(age)
# print(person)

# popitem()方法
# item = person.popitem()
# print(item)
# print(person)

# update()方法
# dict1 = {"name" : "Bob", "age" : 18}
# dict2 = {"gender" : "man", "phone" : "18321224587"}
# dict1.update(dict2)
# print(dict1)

# 集合
# fruits = {'apple', 'orange', 'banana'}

# 集合常用函数和方法
# len()函数
# length = len(fruits)
# print(length)

# add()方法
# fruits.add("grape")
# print(fruits)

# remove()方法
# fruits.remove("apple")
# print(fruits)

# pop()方法
# removed_fruits = fruits.pop()
# print(removed_fruits)
# print(fruits)

# clear()方法
# fruits.clear()
# print(fruits)

# if-elif-else语句
# x = 10
# if x > 0:
#     print("x是正数")
# elif x < 0:
#     print("x是负数")
# else:
#     print("x是零")

# for循环
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)

# while循环
# count = 0
#
# while count < 5:
#     print(count)
#     count += 1

# break
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         break
#     print(num)

# continue
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         continue
#     print(num)

# return
# def add(a,b):
#     return a + b
#
# result = add(3, 5)
# print(result)

# 函数

# 基本函数
# def greet():
#     print("Hello World!")
#
# greet()

# 带参数的函数
# def greet(name):
#     print("Hello " + name + "!")
#
# greet("Alice")
# greet("Bob")

# 返回值的函数
# def add(a, b):
#     return a + b
#
# result = add(2, 3)
# print(result)

# 模块

# os模块
# import os
#
# current_dir = os.getcwd()
# print(current_dir)

# datetime模块
# from datetime import datetime
#
# now = datetime.now()
# print(now)

# 面向对象编程

# 类(Class)和对象(Object)
# class Person: # 定义一个Person类
#
# 属性(Attribute)和方法(Method)
#     def __init__(self, name, age): # 定义一个构造方法,初始化对象属性
#         self.name = name # name属性
#         self.age = age # age属性
#
#     def greet(self): # 定义一个方法
#         print(f"Hello, my name is {self.name} and I am {self.age} years old")

# 创建一个Person对象
# person1 = Person("Alice", 18)
# person1.greet()
# person2 = Person("Bob", 18)
# person2.greet()

