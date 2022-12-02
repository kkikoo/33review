"""multiple decorators at the same w/ more than one""@"""

def with_greeting(func):
    def greet_and_execute(n):
        print('Hello!')
        return func(n)

from datetime import datetime
def with_time_display(func):
    def show_time_and_execute(*args, **kwargs):
        print(f'Current Time: {datetime.now():%I:%M:%S %p}')
        return func(*args, **kwargs)
    return show_time_and_execute

@with_greeting
@with_time_display

def square(n):
    return n * n        # We can decorate a function with more than one decorator.
square(3)
#Hello!
#Current Time: 11:07:18 PM
#9