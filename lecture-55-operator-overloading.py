#             Operator overloading In Python (OOP's)
    
#  Operator overloading lets you define how operators should behave for instances of your own classes, making it possible to use familiar operators with custom objects in a meaningful way.
    
# +, -, *, /

# 10 + 20

# operands : 10, 20
# operator : +


class mycls:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def hlo(self):
        print("this is hlo")
    
    def __add__(self, other):
        x = self.num1 + other.num1
        y = self.num2 + other.num2
        sum = mycls(x, y)
        return sum
    
obj = mycls(10, 20)
obj1 = mycls(20, 40)

c = obj + obj1

print(c.num2)





    