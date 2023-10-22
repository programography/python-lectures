# Type of Parameters:        
    # 1) Positional Parameters
    # 2) Keyword Parameters
    # 3) Default Parameters
    
    # 4) Variable-Length Parameters
    #     a) *args    ()
    #     b) **kwargs : keywrod arbtrary posational arguments  {}
    
# def xyz(a, b):
#     c = a + b
#     print(c)

# xyz(12, 10)


#  a) *args = arbitrary posational arguments  


# def sumthisall(*x):
#     tot = 0
#     for i in x:
#         tot = tot + i
#     print(tot)
    
# sumthisall(12, 10, 12, 19, 78, 2)



# b) **kwargs : keywrod arbtrary posational arguments  {}


def saveinfo(**x):
    print(x)
    
saveinfo(name = "kriss", age = 20)