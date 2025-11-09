import numpy as np

#slice [index]
a = np.arange(10)
print(a)
b = slice(2, 7, 2)
print(type(b)) #slice class
print(a[b])

print(a[2])

# 整数数组索引
print("---part 2----")
x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0,1,2],  [0,1,0]] #three value [0,0] [1,1] [2,0]
print(type(y))
print (y)
print("---part 3----")
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])  #[0,0] [0,2] [3,0] [3,2]
y = x[rows,cols]
print(type(y))
print  ('这个数组的四个角元素是：')
print (y)

#broadcast
print("---part 4----")
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.array([1,2,3])
z = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x + y)
print(x + z)

# nditer
# for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
# for x in np.nditer(a.T, order='C'):C order，即是行序优先；
print("---part 5----")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in np.nditer(a):
    print(x, end=',')
print('\n')
for x in np.nditer(a, order='F'):
    print(x, end=',')
print('\n')
for x in np.nditer(a, order='C'):
    print(x, end=',')
print('\n')

# modify
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：')
print(a)

#array operation
print('----part 6----')
print('---reshape---')
# reshape flat flatten ravel
a = np.arange(8)
print('原始数组：')
print(a)
print('\n')

b = a.reshape(4, 2)
print('修改后的数组：')
print(b)

a = np.arange(9).reshape(3, 3)
print('原始数组：')
for row in a:
    print(row)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)
#flatten ravel return one dim array

print('---transpose---')
# tranpose  self.T  rollaxis swapaxes
a = np.arange(9).reshape(3, 3)
print(a)
print(np.transpose(a))

a = np.arange(2 * 3 * 4).reshape(2, 3, 4)
print(a)
b = np.rollaxis(a, 2, 0)
print(b)
#原轴顺序 [0,1,2] → 移动轴 2 到位置 0 → 新轴顺序 [2,0,1]，对应形状从 (2,3,4) 变为 (4,2,3)。

print("---mod array dim---")
# boardcast  numpy.squeeze (delete one dim) : (1, 3, 3) --> (3, 3)
#广播的意义是避免实际复制数据（仅通过迭代器模拟扩展后的数组），节省内存并简化元素级操作
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
# 对 y 广播 x
b = np.broadcast(x, y)
print(type(b))
print(b.shape)
for element in b:
    print(element)
# return  tuple 元组
# use iter to show data

print("----concatenate array---")
#concatenate
a = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(b)
print('\n')
# 两个数组的维度相同

print('沿轴 0 连接两个数组：')
print(np.concatenate((a, b)))
print('\n')

print('沿轴 1 连接两个数组：')
print(np.concatenate((a, b), axis=1))

print("---split array---")
print("\n")
#numpy.split(ary, indices_or_sections, axis)
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('将数组分为三个大小相等的子数组：')
b = np.split(a, 3)
print(b)
print('\n')

print('将数组在一维数组中表明的位置分割：')
b = np.split(a, [4, 7])
print(b)

print("\n")
print("add(delete) numpy value ")
#resize append insert delete unique
a = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：')
print(a)
print('\n')

print('第一个数组的形状：')
print(a.shape)
print('\n')
b = np.resize(a, (3, 2))

print('第二个数组：')
print(b)
print('\n')

print('第二个数组的形状：')
print(b.shape)
print('\n')
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了

print('修改第二个数组的大小：')
b = np.resize(a, (3, 3))
print(b)