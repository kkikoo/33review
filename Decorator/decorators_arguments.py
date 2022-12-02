"""装饰器@里可加参数：@xxx()"""

"""decorators with arguments的好处：把参数设置在decorator"里，这样可以不让函数写死，例子如下"""

def read_int():
    for _ in range(4):              #这样写死在里面了，只能重试4次
        try:
            return int(input('Enter an integer: '))
        except Exception:
            pass

    return int(input('Enter an integer: '))

# This is a decorator that allows a function to be retried a specified number
# of times when it fails with any kind of exception.  Below is an example of how
# it could be used:
@retry_on_failure(3)            #def retry_on_failure在下面
def read_int():
    return int(input('Enter an integer: '))

def retry_on_failure(times):
    # Ensure that times is converted to an integer.  Note that this conversion
    # will fail if times can't be converted, which naturally handles situations
    # where times is an incompatible type of input.
    times = int(times)

    # We can't retry a negative number of times, and it doesn't make sense to
    # retry zero times, so we should probably disallow that, too.
    if times < 1:
        raise ValueError(f'times must be a non-negative integer, but was {times}')

    # It's important to realize that retry_on_failure is not actually a decorator,
    # but is instead a function that builds and returns a decorator, based on the
    # value of its argument.  This decorate function is that decorator.  It follows
    # similar pattern to the ones we've seen: returning a function that calls the
    # underlying function (in this case, repeatedly, until it succeeds or it's
    # been attempted the specified number of times).
    def decorate(func):

        # This function is the one that's returned by the decorator, which is the
        # one that someone will actually be calling when they call the decorated
        # function they wrote.
        def run(*args, **kwargs):
            for _ in range(times - 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass

            return func(*args, **kwargs)
        return run
    return decorate