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

    def count():
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