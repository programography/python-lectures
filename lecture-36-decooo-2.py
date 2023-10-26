#             Decorators in Python
            
# decorators are primarily used to decorate or enhance the behavior of functions in Python. 


# Decorators with peameters : 

# *args
# **kwargs

def mydoc(fun):
    def xyz(*args, **kwargs):
        print("Welcm to the funcation")
        fun(*args, **kwargs)
        print("thank you for using my funcation")
    return xyz

@mydoc
def sumthis(x, y, z):
    c = x + y + z
    print("the sum is : ", c)
    
sumthis(10, 20, 100)


# sumthis(100, 200)