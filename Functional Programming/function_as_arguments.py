#将lambda当作参数传入别的function

def square(n):
    return n * n

def transform_all(f, values):
    for value in values:
        yield f(value)

list(transform_all(square, [1, 2, 3]))
#[1, 4, 9]
list(transform_all(lambda n: -n, [1, 3, 5]))
#[-1, -3, -5]
