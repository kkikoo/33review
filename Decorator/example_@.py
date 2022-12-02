def with_greeting(func):
    def greet_and_execute(n):
        print('Hello!')
        return func(n)
    return greet_and_execute

@with_greeting
def square(n):
    return n * n

square(3)
#Hello!          # square is really a version of greet_and_execute
#9               # that calls square, so 'Hello!' is printed here.

@with_greeting
def negate(n):
    return -n

negate(3)
#Hello!          # negate has the same greeting behavior as square,
#-3              # but we only had to write it once.

@with_greeting
def multiply(n, m):
    return n * m

multiply(6, 17)
    #Traceback (most recent call last):

    #TypeError: with_greeting.<locals>.greet_and_execute() takes 1 positional argument but 2 were given