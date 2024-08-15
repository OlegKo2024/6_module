print('Атрибуты вне __init__')

class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.fed = True

        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

        if food.edible == True:
            print(f'{self.name} съел {food.name}')


class Plant(Animal):
    edible = False

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    pass


class Mammal(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)                      # Волк с Уолл-Стрит
print(p1.name)                      # Цветик семицветик
print(a1.alive)                     # True
print(a2.fed)                       # False
a1.eat(p1)                          # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)                          # Хатико съел Заводной апельсин
print(a1.alive)                     # False
print(a2.fed)                       # True

print('Атрибуты в __init__')

class Animal:

    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        self.fed = True

        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

        if food.edible == True:
            print(f'{self.name} съел {food.name}')


class Plant(Animal):
    edible = False

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    pass


class Mammal(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)                     # True
print(a2.fed)                       # False
a1.eat(p1)                          # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)                          # Хатико съел Заводной апельсин
print(a1.alive)                     # False
print(a2.fed)                       # True

