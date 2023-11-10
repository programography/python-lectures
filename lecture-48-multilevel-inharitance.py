#              Inheritance in OOP's
# Inheritance in OOP is to establishes a parent-child relationship between classes. It enables the child class to inherit and access the methods and attributes of its parent or base class.

# parent class => base class, superclass
# child class => derived class or subclass.

# Types of inheritance in OOP:
#     1) Single Inheritance
#     2) Multiple Inheritance
#     3) Multilevel Inheritance
#     4) Hierarchical Inheritance
#     5) Hybrid Inheritance

# 1) Single Inheritance : 1 parent have 1 child
# 2) Multiple Inheritance : 1 child have multiple parents

# 3) Multilevel Inheritance: child -> parent -> grandparent

class cls1:
    def mthd1(self):
        print("this is a method 1")
    
    def mthd2(self):
        print("this is a method 2")
        
class cls2(cls1):
    def methd3(self):
        print("this is a method 3")

class cls3(cls2):
    def methd4(self):
        print("this is method 4")

obj = cls3()
obj.mthd1()












