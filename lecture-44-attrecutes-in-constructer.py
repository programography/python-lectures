#             Constructors in OOP's

# A constructor is a special method in a class that is automatically called when an object is created. It is created using the __init__ method and is used to initialize attributes.


class mycls:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def car(self):
        print(self.num1 + self.num2)
    
    def xy(self):
        print(self.num1)
        

obj = mycls(10, 20)
# obj.car()
# obj.xy()

print(obj.num1)