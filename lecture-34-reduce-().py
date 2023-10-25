# higher-order functions :=> used lambda functions (anonymous functions) to perform operations on iterables like lists, tuples, or other sequences. 

# 1) map()
# 2) filter()
# 3) reduce()

# syntex:
#     reduce(lambda funccation, ittrater)


# from functools import reduce

# lst = [1,2, 4, 5, 7, 2, 4, 5, 6, 1]

# data = reduce(lambda x, y : x + y, lst)

# print(data)


from functools import reduce

lst = [2, 3, 4, 6, 100, 2, 45, 12, 67, 3, 4, 1]

data = reduce(lambda x, y : x if x > y else y, lst)

print(data)






