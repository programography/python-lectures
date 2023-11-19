                        Polymorphism
Types of Polymorphism:
    1) Compile time Polymorphism
        1) Operator Overloading
        2) Method overloading
    
    2) Run time Polymorphism
        1) Method Overriding
            
                Duck Typing In Python OOP's
                    
Duck typing is a programming concept in Python that focuses on an object's behavior rather than its type or class. The term "duck typing"' comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." 


class dog:
    def speak(self):
        print("woof")

class cat:
    def speak(self):
        print("mwaww")

class duck:
    def speak(self):
        print("quack")

obj1 = dog()
obj2 = cat()
obj3 = duck()

def animal_sound(x):
    x.speak()

animal_sound(obj3)







