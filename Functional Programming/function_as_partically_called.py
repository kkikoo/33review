#函数部分call，给函数设置一个默认参数

def multiply(n, m):
    return n * m

multiply(3)
#Traceback (most recent call last):
#TypeError: multiply() missing 1 required positional argument: 'm'

#设定n=3
def partially_call(f, n):
    def complete(m):
        return f(n, m)
    return complete

multiply_by_three = partially_call(multiply, 3)
multiply_by_three(8)            #只传m=8，因为n已经默认3
#24