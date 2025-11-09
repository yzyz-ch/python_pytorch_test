import numpy as np

print(np.__version__)


#create new numpy array
#1. the most commonly used method
a = np.array([1, 2, 3])
print(a)
#2. Fixed value
b = np.ones([2, 3])
print(b)
c = np.zeros([2, 3])
print(c)

# ones_like
# zeros_like  parm is array
# empty don't init, random value

#3. from array which is existed
d = [1, 2, 3, 4, 5]
print(type(d))
print(d)
d_array = np.asarray(d)
print(type(d_array))
print(d_array)
# numpy.fromiter  numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。

#from data value arange
e = np.arange(0, 10, 2)
print(e)
f = np.arange(20)
print(f)