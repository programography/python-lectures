#             Constructors in OOP's

# A constructor is a special method in a class that is automatically called when an object is created. It is created using the __init__ method and is used to initialize attributes.

# class xyz:
#     def hlo(self):
#         print("i am a helo method")
    
#     def sumthis(self, a, b):
#         c = a + b
#         print(c)
    
#     def savedata(self):
#         print("i am a save data", a)
        
# obj = xyz()  
# obj.hlo()

# obj.sumthis(10, 20)    

# obj.savedata()    
        


class xyz:
    def __init__(self):
        print("heyyyyyyyyyy")
    
    def hlo(self):
        print("i am a helo method")
    
    def sumthis(self):
        print("this is a funcation too")
    
    def savedata(self):
        print("i am a save data", a)

obj = xyz()  
obj1 = xyz()

