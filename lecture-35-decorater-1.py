#             Decorators in Python
            
# decorators are primarily used to decorate or enhance the behavior of functions in Python. 


def deco(fun):
    def wraprer():
        print("Welcom to my funcation" )
        
        fun()
        
        print("Thak yuu for using my funcation")
    return wraprer

@deco
def myfun():
    print("::i am main funcation::")

myfun()


@deco
def xyz():
    print("hyyyyyyy")
    
xyz()