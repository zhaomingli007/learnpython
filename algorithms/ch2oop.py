#C-2.3
class Flower:
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_petals(self, petals):
        self.petals = petals

    def set_price(self, price):
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price


f = Flower('Rose', 3, 19.0)
print(f.get_name())
print(f.get_price())
f.set_price(20)
print(f.get_price())

#C2.9
