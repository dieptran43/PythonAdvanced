#CreatedBy: LE VAN DIEP

class Greeting:
    count = 0
    def __init__(self, name):
        self.name = name
        #grow param count
        Greeting.count +=  1
    
    def say_hi(self):
        print("Hello: ", self.name)
    
    def say_goodbye(self):
        return "Bye: " + self.name
    
if __name__ == "__main__":
    obj1 = Greeting("Python Advanced by DiepVan IPMan!")
    obj1.say_hi()
    obj1.say_goodbye()
    print("Count: ", Greeting.count)
    print("*" * 30)    
    
    obj1 = Greeting("Developer in Furture!")
    obj1.say_hi()
    print(obj1.say_goodbye())
    print("Count: ", Greeting.count)
    print("*" * 30)    
