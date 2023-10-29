#                     partial function,

the functools module provides the partial function, which allows you to fix a specific number of arguments of an existing function, creating a new function with the fixed arguments. 


def xyz(a, b):
    c = a ** b
    print(c)

# xyz(3, 3)

# xyz(12, 3)

from functools import partial

# zx = partial(existing funcation, add fixed arguments, )

seq = partial(xyz, b = 2)

seq(4)







# print(2 ** 10)

# 2 x 2x 2



