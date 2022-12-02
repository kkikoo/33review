# 1.通过super() 来调用父类的__init__ 构造方法：

class Person():
    def __init__(self):
        print('我是Peson的__init__构造方法')


class Student(Person):
    def __init__(self):
        super().__init__()
        print('我是Student的__init__构造方法')

stu = Student()
#---------------------------------------
#我是Person的__init__构造方法
#我是Student的__init__构造方法


# 2 通过super() 来调用与子类同名的父类方法
# 2.1 单继承
# 在单继承中 super 就像大家所想的那样，主要是用来调用父类的方法的。

class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3
b = B()
b.add(2)
print(b.n)

#self is <__main__.B object at 0x106c49b38> @B.add
#self is <__main__.B object at 0x106c49b38> @A.add
#8

#1、super().add(m) 确实调用了父类 A 的 add 方法。
#2、super().add(m) 调用父类方法 def add(self, m) 时, 此时父类中 self 并不是父类的实例而是子类的实例, 所以 b.add(2) 之后的结果是 5 而不是 4 。
