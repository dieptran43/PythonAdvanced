#CreatedBy: LE VAN DIEP

#include math for sqrt()
import math

class Triangle:
    #init class with 3 param a,b,c
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    #calulator with P perimeter , S acreage
    def perimeter(self):
        return self.a + self.b + self.c

    def acreage(self):
        p = self.perimeter()/2
        return math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
    
    def display(self):
        print("Sides are a,b,c: ", self.a, self.b, self.c, ", P: ", self.perimeter(), ", S: ",round(self.acreage(),2))

#create object with class Triangle  
if __name__ == "__main__":
    obj1 = Triangle(1,3,4)
    obj2 = Triangle(2,3,4)
    obj3 = Triangle(3,3,4)
    obj4 = Triangle(4,3,4)

    print("Triangle 1: ", obj1.perimeter())
    print("Acreage 1: ", obj1.acreage())
    print("Triangle 2: ", obj2.perimeter(), " - Acreage 2: ", obj2.acreage())
    print("Triangle 3: ", obj3.perimeter(), " - Acreage 3: ", round(obj3.acreage(),2))
    print("Triangle 4: ", obj4.perimeter(), " - Acreage 4: ", round(obj4.acreage(),3))
    obj4.display()


    


