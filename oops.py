class Dog:
    def __init__(self, breed, age, color):
        self.bread = breed
        self.age = age
        self.color = color


class cat:
    def __init__(self,name, gender, is_wild):
        self.name = name
        self.gender = gender
        self.is_wild = is_wild

class Burger:
    def __init__(self,bread, topping, filling, is_veg, price):
        self.bread = bread
        self.topping = topping
        self.filling = filling
        self.is_veg = is_veg
        self.price = price
#use classes to creat objects

tiger = Dog('German Shepherd', 2, 'Golden')
sheru = Dog('Pug',3, 'black')
tommy=Dog('labrador',1, 'white')

mau=cat('mau', 'M', False)
mimi=cat('mimi', 'F', False)
max=cat('max', 'M', True)
oreo=cat('oreo','F',False)

burger1=Burger('brown', 'lettuce', 'veg',True, 50)
burger2=Burger('brown','chees','chicken',False, 100)

print("tiger is a", tiger.breed,"dog")
