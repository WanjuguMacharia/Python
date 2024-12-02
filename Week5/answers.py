class Smartphone:

    def __init__(self, brand, storage, color):

        self.brand = brand
        self.storage = storage
        self.color = color

    def smart1(self):
        return f" This brand {self.brand}, {self.storage}, {self.color} rocks"
    
    def smart2(self):
        return f"This brand {self.brand}, {self.storage}, {self.color} has the best camera"

phone1 = Smartphone('samsung', 256, 'blue')
phone2 = Smartphone('Oppo', 128, 'black')

print(phone1.smart1())
print(phone2.smart2())


#Question 2

class cow:

    def legs(self):
        return f"A cow has 4 legs"
    

class snake:
    def legs(self):
        return f'A snake has 0 legs'
    

class spider:
    def legs(self):
        return f'A spider has 8 legs'
    

for animal in [cow(), snake(), spider()]:
    print(animal.legs())