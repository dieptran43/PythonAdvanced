#CreatedBy: LE VAN DIEP

class DOG:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Gou gou...")

class CAT:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Miu o miu o...")
    
if __name__ == "__main__":
    obj1 = DOG("DOG 1")
    obj1.say_hi()
    print("*" * 30)

    list1 = []
    list1.append(DOG("DOG 2"))
    list1.append(CAT("CAT 1"))
    for animal in list1:
        if isinstance(animal,DOG)
            print("It is DOG")
        animal.say_hi()

