            #   Abstraction in OOP's (Python)

# (Data Hidding)

# Abstraction in Python OOP is the process of simplifying complex systems by creating abstract classes that define a common interface. It hides the implementation details, allowing the use of high-level concepts without concern for internal workings.


# 1) Abstraction
# 2) Abstract classes
# 3) Abstract Methods
# 4) Interfaces


from abc import ABC, abstractmethod

# interface
class cls1(ABC):
    @abstractmethod
    def mthd1(self):
        pass
    
    @abstractmethod
    def mthd2(self):
        pass
    
    @abstractmethod
    def car(self):
        print("ok")


class cls2(cls1):
    def mthd3(self):
        print("this is a mthod 3")
    
    def mthd1(self):
        print("this is ok")
    
    def mthd2(self):
        print("this is also ok")

obj = cls2()








