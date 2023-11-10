#              Inheritance in OOP's
# Inheritance in OOP is to establishes a parent-child relationship between classes. It enables the child class to inherit and access the methods and attributes of its parent or base class.

# parent class => base class, superclass
# child class => derived class or subclass.

# Types of inheritance in OOP:
    # 1) Single Inheritance
    # 2) Multiple Inheritance
    # 3) Multilevel Inheritance
    # 4) Hierarchical Inheritance
    # 5) Hybrid Inheritance
    
class cls1:
    def __init__(self, a, b):
        self.name = a
        self.age = b
        # self.number = c
    
    def saveinfo(self):
        print(f"user name is : {self.name} and user age is {self.age}.")

obj = cls1("kriss", 20)
obj.saveinfo()    

obj1 = cls1("moris", 30) 
obj1.saveinfo()
    

class cls2(cls1):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.number = c
    
    def saveinfo(self):
        print(f"user name is : {self.name} and user age is {self.age} and number : {self.number}.")
    

objx = cls2("hlo", 20, 9287349864)
objx.saveinfo()
