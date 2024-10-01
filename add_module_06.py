print('Задание "Они все так похожи"')
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)

# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать
# массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

from math import pi, sqrt
class Figure:
    sides_count = 0

    def __init__(self, __sides: list[int], __color: list[int, int, int], filled: bool = True):
        if len(__sides) == self.sides_count:
            self.__sides = __sides
        else:
            self.__sides = [__sides[0]] * self.sides_count
        self.__color = self.__is_valid_color(__color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color: list[int, int, int]):
        if isinstance(color, list) and len(color) == 3:
            if all(isinstance(c, int) and 0 <= c <= 255 for c in color):
                return color
        return None
        # print(f'{color} должен быть список (R, G, B) в интервале 0-255')
        # return None

    def set_color(self, color: list[int, int, int]):
        if self.__is_valid_color(color):
            self.__color = color
        else:
            # print(f'{color} не может быть изменен, должен быть список (R, G, B) в интервале 0-255')
            return self.__color

# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
# положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях
    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            if all(isinstance(sides, int) and sides > 0 for sides in args):
                return True
        return False


# Метод get_sides должен возвращать значение я атрибута __sides.
    def get_sides(self):
        return self.__sides

# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не
# изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
                self.__sides = list(new_sides)
        return self.__sides

# Метод __len__ должен возвращать периметр фигуры.
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    def __radius(self):
        return len(self) / (2 * pi)

    def get_square(self):
        return pi * self.__radius() ** 2

class Triangle(Figure):
    sides_count = 3

# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

    def get_square(self):
        sides = self.get_sides()  # Используем публичный метод для получения сторон
        p = sum(sides) / 2  # Полупериметр
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5  # Формула Герона

class Cube(Figure):
    sides_count = 12

# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.

    def all_equal(self):
        return all(sides == self.get_sides()[0] for sides in self.get_sides())

    def get_volume(self):
        if self.all_equal():
            sides = self.get_sides()
            return sides[0] ** 3


painted = Figure([10], [100, 100, 100])
print(painted.get_color())

painted_01 = Figure([10], [200, 100, 100])
print(painted_01.get_color())

circle1 = Circle([10], [200, 200, 100]) # (Цвет, стороны)
print(circle1.get_color())
cube1 = Cube([6],[222, 35, 130])
print(cube1.get_color())

print('Проверка на изменение цветов:')
circle1.set_color([55, 66, 77]) # Изменится
print(circle1.get_color())
cube1.set_color([300, 70, 15]) # Не изменится
print(cube1.get_color())

print('Проверка на изменение сторон:')
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print('Проверка периметра (круга), это и есть длина:')
print(len(circle1))
print(circle1.get_square())
trianle1 = Triangle([10, 10, 10], [200, 200, 100])
print(trianle1.get_color())
trianle1.set_color([40, 70, 15])
print(trianle1.get_color())
trianle1.set_sides(5, 5, 5)
print(trianle1.get_sides())

print(trianle1.get_square())

print('Проверка объёма (куба):')
print(cube1.get_sides())
print(cube1.all_equal())
print(cube1.get_volume())