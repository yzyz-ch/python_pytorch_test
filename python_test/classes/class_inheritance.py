# class person:
#     age = 0
#     height = 0
#     weight = 0
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def speak(self):
#         print("person name is " + self.name)
#         print("person age is " + str(self.age))
#         print("person height is " + str(self.height))
#         print("person weight is " + str(self.weight))
#
#
# class student(person):
#     grade = 0
#     def __init__(self, name, age, height, weight, grade):
#         person.__init__(self, name, age, height, weight)
#         self.grade = grade
#
#     def speak(self):
#         print("student grade is " + str(self.grade))
#         print("student name is " + self.name)
#         print("student age is " + str(self.age))
#         print("student height is " + str(self.height))
#         print("student weight is " + str(self.weight))
#
#     def goschool(self):
#         print("student goschool")
#
#
# student1 = student("shawn", 25, 180, 140, 12)
# per0 = person("carry", 25, 180, 140)
#
# student1.speak()
# student1.goschool()
#
# per0.speak()


#规则写法
# 父类：Person（遵循大驼峰命名法）
class Person:
    # 构造方法：添加类型注解，明确参数类型
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name: str = name  # 实例属性添加类型注解
        self.age: int = age
        self.height: int = height  # 单位默认按代码逻辑设为cm
        self.weight: int = weight  # 单位默认按代码逻辑设为kg

    # 实例方法：返回值为None（无返回）
    def speak(self) -> None:
        print(f"Hello {self.name}!")  # 推荐用f-string，比+拼接更简洁
        print(f"Your age is {self.age}")
        print(f"Your height is {self.height} cm")
        print(f"Your weight is {self.weight} kg")


# 子类：Student（继承自Person）
class Student(Person):
    # 子类构造方法：新增grade参数，添加类型注解
    def __init__(self, name: str, age: int, height: int, weight: int, grade: int) -> None:
        # 用super()调用父类构造方法，无需传self，适配多继承场景
        super().__init__(name, age, height, weight)
        self.grade: int = grade  # 子类新增实例属性

    # 重写父类speak方法
    def speak(self) -> None:
        # 优先打印子类特有属性
        print(f"Student grade is {self.grade}")
        # 打印继承的父类属性
        print(f"Student name is {self.name}")
        print(f"Student age is {self.age}")
        print(f"Student height is {self.height} cm")
        print(f"Student weight is {self.weight} kg")

    # 子类特有方法
    def go_school(self) -> None:
        print(f"Student {self.name} goes to school")


# 代码测试（实例化与方法调用）
if __name__ == "__main__":
    # 实例化子类Student
    student1: Student = Student("shawn", 25, 180, 140, 12)
    # 实例化父类Person
    per0: Person = Person("carry", 25, 180, 140)

    # 调用子类方法
    student1.speak()
    student1.go_school()

    # 分隔线：优化输出可读性
    print("-" * 30)

    # 调用父类方法
    per0.speak()


