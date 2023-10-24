# higher-order functions :=> used lambda functions (anonymous functions) to perform operations on iterables like lists, tuples, or other sequences. 

# 1) map()
# 2) filter()
# 3) reduce()


# 2) filter():

# synetx :
#     filter(lambda funcation, itrater)

# print(7 % 2 == 0)

# x = [2, 1, 2, 34, 56, 3, 4, 6, 8, 2, 3, 6, 5, 8, 1, 135, 10]


# data = filter(lambda i : i % 2 != 0, x)

# print(list(data))



lst = [1, 2, -12, -1, 12, -90, 89, -100, 3]

# filter(lambda funcation, itrater)

newlst = filter(lambda x : x < 0, lst)

print(list(newlst))

