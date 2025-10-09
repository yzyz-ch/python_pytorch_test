#iter
list1 = [1,2,3,4,5,6,7,8,9]
it = iter(list1)
print(next(it))
print(next(it))
print('---------')

it1 = iter(list1)
for i in it1:
    print(i)



#generator yield
print('---------')
#yield 用于定义生成器函数
#当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
#每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
#调用一个生成器函数，返回的是一个迭代器对象。
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 创建生成器对象
generator = countdown(5)

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1


