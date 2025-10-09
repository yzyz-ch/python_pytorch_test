# open(filename, mode)
f = open('./files/files.txt', 'r')
print(type(f))
str = f.read()
str1 = f.readline()
print(str)
print("-----")
print(f.tell())
print(str1)
f.close()

f1 = open('./files/files1.txt', 'w')
f1.write("hello world")
f1.close()



