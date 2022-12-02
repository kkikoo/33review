"""非常重要"""
#如想把class像函数那样call，不能直接call class的名！
#用callable()，注意：Integers are not callable.

class Square:
    def __call__(self, n):
        return n * n

Square(3)
    #Traceback (most recent call last):

    #TypeError: Square() takes no arguments
                  # This is an attempt to construct a Square object, rather than
                  # a call to one.  Since Square has no __init__ method,
                  # arguments can't be passed when constructing one.
s = Square()
                  # But we can construct a Square object and store it in a variable.
callable(s)
#True             # Square objects are callable, because of the __call__ method.

s(3)
#9                # Calling a Square object calls its __call__ method.


