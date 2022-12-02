any(x > 0 for x in [-1, -2, -3, -4])
#False
any(x > 0 for x in [-1, -2, -3, -4, 0, 1, 3])
#True
all(x > 0 for x in [-1, -2, -3, -4, 0, 1, 3])
#False
all(x > 0 for x in [1, 3, 5, 7])
#True

#Missing built-in function, tells you whether none of an iterable's values are truthy
none(x > 0 for x in [-1, -2, -3, -4])
#True
none(x > 0 for x in [-1, -2, -3, -4, 0, 1, 3])
#False