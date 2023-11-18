# Types of Polymorphism:
#     1) Compile time Polymorphism
#         1) Operator Overloading
#         2) Method overloading
    
#     2) Run time Polymorphism
#         1) Method Overriding

#              Method  Overriding In Python (OOP's)
        
#   Method overriding in Python OOP is the process of redefining a method in a subclass that is already defined in its superclass. The overridden method in the subclass has the same name and parameters as the method in the superclass, allowing the subclass to provide its own implementation.



# a = 10

# a = 20

# print(a)

class mycls:
    def car(self):
        print("this is a car")
    
    def bus(self):
        print("this is a bus")

class cls1(mycls):
    def train(self):
        print("this is a train")
    
    def bus(self):
        print("noooooooo")


obj = cls1()
obj.bus()
