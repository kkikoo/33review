"""functools.reduce"""
#把多个object归约变成一个
#reduce的规则是根据lambda后的表达式

import functools

functools.reduce(lambda a, b: a + b, [1, 2, 3, 4])
#10                  # Adding the elements together yields their sum.
functools.reduce(lambda a, b: a + b, [[1, 2], [3, 4], [5, 6]])
#[1, 2, 3, 4, 5, 6]  # Adding lists together flattens them.
functools.reduce(max, [3, 11, 7, 2, 1, 9])
#11                  # If each combining operation returns the larger of the new value
                     # and the largest so far, we'll have determined their maximum.

from functools import reduce
"""1. int的累积:列表里面整数累加"""
a=[1,3,5]
b=reduce(lambda x,y:x+y,a)
print('1.列表里面整数累加==:',b)
#1.列表里面整数累加==: 9

"""2. list的累加：列表里面的列表相加"""
a=[[1,3,5],[6]]
b=reduce(lambda x,y:x+y,a)
print('2.列表里面的列表相加—:',b)
#2.列表里面的列表相加—: [1, 3, 5, 6]

a=[[["abc","123"],["def","456"],["ghi","789"]]]
b=reduce(lambda x,y:x+y , a )
print('列表里面的列表相加—:',b)
#列表里面的列表相加—: [['abc', '123'], ['def', '456'], ['ghi', '789']]

"""3. tuple的累加：列表里面的元组相加"""
a=[("abc","123"),("def","456"),("ghi","789")]
b=reduce(lambda x,y:x+y , a )
print('3.列表里面的元组相加!!',b)
#3.列表里面的元组相加!! ('abc', '123', 'def', '456', 'ghi', '789')

"""4. 字符串的累加"""
a=['abc','def','hij']
b=reduce(lambda x,y:x+y,a)
print('4.列表里面字符串的累加:~~',b)
#4.列表里面字符串的累加:~~ abcdefhij

a=('abc','def','hij')
b=reduce(lambda x,y:x+y,a)
print('元祖里面字符串的累加:~~',b)
#元祖里面字符串的累加:~~ abcdefhij

a=[['abc','def','hij']]
b=reduce(lambda x,y:x+y,a)
print('嵌套列表里面字符串的累加:~~',b)
#嵌套列表里面字符串的累加:~~ ['abc', 'def', 'hij']

"""总结：
1.functools函数；reduce分解；lambda 匿名函数；x,y:x+y 表达式 (reduce(lambda x,y:x+y))
2.使用functools.reduce，要是整数就累加；
3.使用functools.reduce，要是字符串、列表、元祖就拼接（相当脱了一层外套）
"""