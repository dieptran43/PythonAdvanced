#CreatedBy: LE VAN DIEP

#include math for sqrt()
import math

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    #__str__ to define output
    def __str__(self):
        return str(self.a)+ "/" + str(self.b)
    
    #self: current object(1), other: other object(2)
    def __add__(self, other):
        tmpAbove = (self.a * other.b) + (other.a * self.b)
        tmpBelow = self.b * other.b 
        return str(tmpAbove) + "/" + str(tmpBelow)

if __name__ == "__main__":
    obj1 = Fraction(2,3)
    obj2 = Fraction(4,5)
    #use __str__
    print("Fraction 1: ", obj1)
    print("Fraction 2: ", obj2)
    #use __add__
    print("Result case 1: ", obj1.__add__(obj2))
    print("Result case 2: ", obj1 + obj2)
