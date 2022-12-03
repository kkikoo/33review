"""非常重要"""
"""把class实现成decorator"""

#将实现__call__的class作为decorator
class InterestingIdea:
    def __init__(self, func):
        pass
    def __call__(self, *args, **kwargs):
        return 'Boo!'

@InterestingIdea        #调用整个class，为了实现 def __call__
def square(n):
    return n * n

type(square)
#<class '__main__.InterestingIdea'>
square(3)
#Boo!

"""重点！"""
class WithCallsCounted:
    def __init__(self, func):
        self._func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._func(*args, **kwargs)

    def count(self):
        return self._count                  #让函数记住每call一下，call了几次

@WithCallsCounted

def square(n):                              #squre本身没有count()的，但是decorator @WithCallsCounted后，
    return n * n                            #可以无中生有，把def count()的方法赋给def square
                                            #将square变成了WithCallsCounted的object，square可以算square平方本身和被count了多少次
square(3)
#9  # The decorated square function acts like the original one when it's called.

square.count()
#1  # But square also knows how many times it's been called.
square(5)
#25  # Does it really?
square.count()
#2  # Yes, it does!
type(square)
#<class 'call_counting.WithCallsCounted'>    # And this is why.

"""记住背诵"""
#     @fields(('name', 'age'))
#     class Person:
#         pass
#
# then we expect Person to have three features automatically:
#
# * An __init__ method that, if passed two positional arguments, will assign
#   the value of the first argument into a _name attribute and the value of
#   the second argument into an _age attribute.
# * A name() method that returns the value of the _name attribute.
# * An age() method that returns the value of the _age attribute.


def fields(field_names):
    field_names = list(field_names)
    def make_field_getter(field_name):
        def get_field(self):
            return getattr(self, f'_{field_name}')
        return get_field

    def decorate(cls):
        for field_name in field_names:
            setattr(cls, field_name, make_field_getter(field_name))

        def __init__(self, *args):
            for field_name, arg in zip(field_names, args):
                setattr(self, f'_{field_name}', arg)            #此处的set attribute可以修改下面line83 class的变量

        cls.__init__ = __init__
        return cls
    return decorate

@fields(('name', 'age'))
class Person:
    pass

p = Person('Boo', 13, 18)
p.name()
#'Boo'
p.age()
#13
p.height()
#18

#setattr() 和 getattr()的用法：
class A(object):
    bar = 1

a = A()
getattr(a, 'bar')          # 获取属性 bar 值
#1
setattr(a, 'bar', 5)       # 设置属性 bar 值
a.bar
#5

