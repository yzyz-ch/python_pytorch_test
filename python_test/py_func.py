def add(x,y):
    return x+y

print(add(1,2))
print(add(3,4))

print('------------')

#参数传递
#可更改(mutable)与不可更改(immutable)对象
#strings, tuples, 和 numbers 是不可更改的对象，在函数内部会重新生成
#可变的直接修改即可
def change(a):
    print('func intern id1:', id(a))  # 指向的是同一个对象
    a = 10
    print('func intern id1:',id(a))  # 一个新对象

a = 1
print('func extern id1:',id(a))
change(a)
print('------------')
#使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
# 调用printme函数
printme(str="菜鸟教程")

# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return

# 调用printinfo函数
printinfo(age=50, name="runoob")
print('------------')

#不定长参数
#需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名
'''
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

#加了两个星号 ** 的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo(1, a=2, b=3)
printinfo(1, r=2, e=3, f=4, i=8)
printinfo(1, **{'a':1, 'b':2, 'c':3, 'd':4})

print('------------')
#lambda

