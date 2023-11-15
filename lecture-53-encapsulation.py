                # Encapsulation In Python

# to bindup multiple things in a single unit.

# In Python, encapsulation is a concept in object-oriented programming (OOP) that involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class. Encapsulation helps in hiding the internal details of an object.

# 1) Encapsulation
# 2) Access Spacifires:
#     1) Public mambers
#     2) Protected Mambers  _
#     3) Private mambers  __


class cls1:
    def __init__(self):
        self.__name = "kriss"
        self.age = 20
    
    def __mthd1(self):
        print("this is mrthod 1", self.__name)

class cls2(cls1):     
    def mthd2(self):
        print("this is method 2", self._name)
    
    def mthd3(self):
        print("this is method 3")

obj = cls1()
obj.__mthd1()
# print(obj.__name)












