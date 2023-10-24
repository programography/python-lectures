# higher-order functions :=> used lambda functions (anonymous functions) to perform operations on iterables like lists, tuples, or other sequences. 

# 1) map()
# 2) filter()
# 3) reduce()

# 1) map() : 
    
#     map(lambda funcation, itrater)
    

# lambda argument : expression

# a = [1, 2, 3, 4, 5, 6, 7, 8]

# xyz = map(lambda i : i + 10, a)


# print(list(xyz))


xy = [3, 4, 5, 6, 7, 8, 9, 12, 10]


x = map(lambda i : i - 3, xy)

print(tuple(x))


# print(2 ** 4)

