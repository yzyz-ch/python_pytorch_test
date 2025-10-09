# str() trans  datatype to str
# repr() return str , can use eval to create obj
# a obj can calling __repr__() by using repr
s = 'Hello, Runoob'
print(s)
str(s)
s1 = "\tHello, Runoob\n"
print(s1)
print(str(s1))
print(repr(s1))

print("---------------")

name = "Alice"
print(f"Name: {name!r}")  # 输出: Name: 'Alice'


print("---------------")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"str({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
# pirnt(p)
print(str(p))
print(repr(p))  # 输出: Point(3, 4)
print("---------------")

p = Point(3, 4)
p_repr = repr(p)  # 'Point(3, 4)'
print(p_repr)
new_p = eval(p_repr)
print(new_p)  # 输出: Point(3, 4)
print(id(p))
print(id(new_p))
