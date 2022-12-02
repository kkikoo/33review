#lambda: 匿名函数，定义lambda时不需要函数名，不像def function
"""
lambda格式：name = lambda[list] : 表达式
ex. square = lambda n : n * n

lambda用法：用于一个function且只有一个expression，把一堆话用lambda变成一句expression
!注意！表达式expression不可有return
"""

make_reversed_list = lambda *values: list(reversed(values))
make_reversed_list(1, 2, 3, 4, 5)
#[5, 4, 3, 2, 1]

make_dict = lambda **kwargs: dict(kwargs)
make_dict(a = 1, b = 2, c = 3)
#{'a': 1, 'b': 2, 'c': 3}

"""表达式前也可以加*或**，**kwargs create a dict"""