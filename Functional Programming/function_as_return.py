#function returns another function, 每次return的function，都是一个全新的object，多次调用return的function虽然功能一样，但不相等！

def make_function():
    def another_function():
        return 'Hello Boo!'
    return another_function

make_function
#<function make_function at 0x000001F29D48DCF0>
make_function()
#<function make_function.<locals>.another_function at 0x000001F29D48D000>
make_function()()
#'Hello Boo!'
