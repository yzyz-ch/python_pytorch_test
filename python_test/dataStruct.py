#this file is coded for learning python datastruct
#common datastruct : list tuple dictionary set
# list [] 增add 删del remove 改mod 查[index]
print('list')
list = [1,2,3,4,5,6,7,8,9]
print(list)
print(len(list))
print(list[0])
list.append(10)
print(list)
list.remove(10)
print(list)
del list[len(list) - 1]
print(list)
list.reverse()
print(list)

#tuple () only can view value by [index]
print('tuple')
tuple1 = (1,2,3,4,5,6,7,8,9)
print(tuple1)
print(tuple1[0])
print(len(tuple1))
tuple_list = tuple(list)
print(tuple_list)

#dictionary  {}
print('dictionary')
tinydict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(tinydict)
tinydict['d'] = 6
print(tinydict)
tinydict.pop('d')
print(tinydict)
tinydict.popitem()
print(tinydict)
tinydict.clear()
print(tinydict)
tinydict.update({'a':1, 'b':2, 'c':3, 'd':4})
print(tinydict)

#set no same value
print('set')
set1 = {1,2,3,4,5,6,7,8,9}
print(set1)
set1.add(11)
print(set1)
set1.remove(11)
print(set1)
set1.pop()#random remove
print(set1)
print(1 in set1)
set1.remove(8)
print(set1)
set2 = {1,2,3,4,5,6,7,8,9,10}
set1.update(set2)
set1.update()
print(set1)

#推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)

listdemo = ['Google','Runoob', 'Taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict)

setnew = {i**2 for i in (1,2,3)}
print(setnew)





