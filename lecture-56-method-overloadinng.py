# Types of Polymorphism:
#     1) Compile time Polymorphism
#         1) Operator Overloading
#         2) Method overloading


#         Method  overloading In Python (OOP's)
        
# When a class can have multiple methods with the same name but different signatures (different parameters). This allows a class to perform different actions based on the number or types of parameters passed to the method.


class mycls:
    def sumthis(self, a, b, c):
        xyz = a + b + c
        print(xyz)
    
    def sumthis(self, a, b):
        xyz = a + b
        print(xyz)
    
    def sumthis(self, a):
        xyz = a
        print(xyz)

obj = mycls()

obj.sumthis(10, 30)



# a = 10

# a = 100

# print(a)




class mycls:
    def sumthis(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            xyz = a + b + c
            print(xyz)
        
        elif a != None and b != None:
            xyz = a + b
            print(xyz)
        
        elif a != None:
            print(a)



obj = mycls()

obj.sumthis(10, 20, 30)








