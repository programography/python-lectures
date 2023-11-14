            #   Abstraction in OOP's (Python)

# (Data Hidding)

# Abstraction in Python OOP is the process of simplifying complex systems by creating abstract classes that define a common interface. It hides the implementation details, allowing the use of high-level concepts without concern for internal workings.


# 1) Abstraction
# 2) Abstract classes
# 3) Abstract Methods
# 4) Interfaces


# abc = abstract base class


from abc import ABC, abstractmethod

class cls1(ABC):
    @abstractmethod
    def car(self):
        pass
    
    @abstractmethod
    def bus(self):
        pass

class cls2(cls1):
    def train(self):
        print("this is a train")
    
    def car(self):
        print("this is car from child class")
    
    def bus(self):
        print("helo")

obj = cls2()
obj.car()




