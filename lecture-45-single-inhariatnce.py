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

class parentclass:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def mthd1(self):
        print("this is method 1")


class chidclass(parentclass):
    def mthd2(self):
        print(self.num1 + self.num2)
    
    def mthd3(self):
        print("i am method 3")

obj = chidclass(20, 67)
obj.mthd1()

obj.mthd2()









