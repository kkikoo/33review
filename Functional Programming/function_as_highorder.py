"""非常重要"""
#f(g(n)) 嵌套函数

def compose(f, g):
    def execute(n):
        return f(g(n))
    return execute

double_square = compose(lambda n: n * 2, lambda n: n * n)
double_square(3)
#18
double_square(5)
#50

formatted_length = compose(len, str)
formatted_length(1)
#1          # When formatted, 1 becomes '1', which has length 1.
formatted_length([1, 2])
#6          # When formatted, [1, 2] becomes '[1, 2]', which has length 6.

#不止一个函数的话记得加*符号表示多个函数
#重要重要#

def make_pipeline(first, *rest):            #first函数单独用，*rest为一个整体一起用
    def execute_pipeline(n):                #第一个函数运行
        current = first(n)
        for f in rest:                      #对于每一个rest里的函数依依运行
            current = f(current)            #用current迭代前一个函数
        return current
    return execute_pipeline

square_of_string_length = make_pipeline(str, len, square)
square_of_string_length(10)            #str=10，len=2，square=4
#4
square_of_string_length(100)
#9


"""map()的用法: 把每一组函数依依映射在lambda或def里对应的element"""
list(map(lambda a, b, c: a + b * c, [1, 3, 5], [2, 4, 8], [-1, 1, -1]))
#[-1, 7, -3]        # 1 + (2 * -1) = -1,  3 + (4 * 1) = 7,  5 + (8 * -1) = -3
list(map(lambda a, b: a * b, [1, 2, 3], [4, 5]))
#[4, 10]            # 1 * 4 = 4,  2 * 5 = 10
                    # Once one iterable runs out of elements, that's the end of the output.

"""filter()的用法: 仅取出符合条件的部分"""
def is_positive(n):
    return n > 0

list(filter(is_positive, [1, -2, 3, -4, 5, -6]))
#[1, 3, 5]          #When the function returns a truthy result, we keep the value. Otherwise, it's discarded.
list(filter(negate(is_positive), [1, -2, 3, -4, 5, -6]))
#[-2, -4, -6]       # The negate function we wrote previously comes in handy here.



