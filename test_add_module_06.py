print('Новое')
print('Варианты наследования на пока')
'''
- Простой: прямая последовательность от родителя до крайнего дочернего: Animals - Birds(Animals) - Beasts(Birds)
- С __init__: кака выше, __init__ в родителе, объект дочернего класса, передает аргументы в параметры __init__ родителя
- С __init__ с разными параметрами родителя и дочки: __init__ в обоих классах, у дочки все параметры с передачей через
название класса родителя Animal. или super(). аргументов параметрам родителя. При super(). self не указывается
- С __init__  множественное наследование моя реализация: дочка в __init__ имеет все параметры, часть использует 
в своем __init__, часть передает в несколько родительских (указанных в классе в скобках классов наследования),
при этом аргументы передаются прямым наследникам через super()., а не прямым указанием названия класса родителя
- С __init__  множественное наследование лекция: как и выше, но сначала все передаваемые передаются родителю, далее 
родитель, часть обрабатывает своим __init___ у себя, а часть передает в __init__ родителю дочернего класса
- С __init__ без наследования см. module_05: new_user = User(nickname, password, age) создается в не связанном 
классе, но ссылается в методе на класс по которому создается объект
'''
print('Дизайн конструктора __init__')
'''
- см. class Figure, def __is_valid_color: прежде чем принять значение проводится проверка на соответствие типу,
получается по сути круг, мы говорим, что self.__color, будет то, что взяв аргументы self объекта, пройдет через функцию
__is_valid_color, при этом параметр color в __is_valid_color, примет переданный аргумент параметром __color и вернет 
значение, которое и будет принято как self.__color. get_color же это getter, который просто выводит данное значение.
'''
print('Варианты и ошибки по циклам - логика пока страдает')
'''
- см. class Figure, def __is_valid(self, color):
'''

# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то
# создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

from math import pi, sqrt
class Figure:
    sides_count = 0

    def __init__(self, __sides: list[int], __color: list[int, int, int], filled: bool = True):
        if len(__sides) == self.sides_count:    # проверка на кол-во переданных параметров, корректировка кол-ва
            self.__sides = __sides
        else:
            self.__sides = [__sides[0]] * self.sides_count
        self.__color = self.__is_valid_color(__color)   # в отношении объекта self, run the method с параметром __color
        self.filled = filled


# Когда в конструкторе (`__init__`) класса `Figure` вызывается `self.__is_valid_color(__color)`, происходит следующе:
# - `self` указывает на текущий экземпляр класса, который создаётся в данный момент.
# - `__color` — это аргумент, который был передан в конструктор, представляющий цвет в формате RGB.
# далее после проверки:
# В строке `self.__color = self.__is_valid_color(__color)`, результат работы метода `__is_valid_color` присваивается
# атрибуту `__color` текущего экземпляра `self`. - Если входной цвет был валидным, `self.__color` получит это значение

    def get_color(self):
        return self.__color

# Задание: Метод __is_valid_color - служебный, принимает параметры r, g, b, проверяет корректность переданных значений
# перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255
# (включительно)
    def __is_valid_color(self, color):
        if isinstance(color, list) and len(color) == 3:
            if all(isinstance(c, int) and 0 <= c <= 255 for c in color):
                return color  # Возвращаем валидный цвет
        # Если цвет недействителен
        # print(f'{color} must be a list of three integers (R, G, B) in the range 0-255.')
        # return None  # Возвращаем цвет по умолчанию

    # def __is_valid(self, color):
    #     if isinstance(color, tuple) and len(color) == 3:
    #         for c in color:
    #             if not (isinstance(c, int) and 0 <= c <= 255):
    #                 # Если хотя бы один компонент невалиден, возвращаем (250, 250, 250)
    #                 return (0, 0, 0)
    #                 # Если все компоненты валидны, возвращаем (10, 10, 10)
    #         return color
    #     # Если color не кортеж, возвращаем (250, 250, 250)
    #     return (0, 0, 0)

# Задание: Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
# предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.

    def set_color_00(self, color):
        if isinstance(color, list) and len(color) == 3:
            if all(isinstance(c, int) and 0 <= c <= 255 for c in color):
                self.__color = color
                return
        # print(f'{color} must be a list of three integers (R, G, B) in the range 0-255.')
        return self.__color

    def set_color_01(self, color: list[int, int, int]):
        valid_color = self.__is_valid_color(color)
        if valid_color is not None:
            self.__color = color
        else:
            # print(f'{color} не может быть изменен, должен быть список (R, G, B) в интервале 0-255')
            return self.__color
# Введя новую переменную `valid_color` мы запускаем метод self.__is_valid_color (метод класса), передав ему значения
# color. Как результат, `valid_color` принимает значение применения метода. Результат может быть: None или валидный
# список в формате RGB. В зависимости от того, какое значение примет valid_color` мы выполняем условие задания
    def set_color(self, color: list[int, int, int]):
        if self.__is_valid_color(color):    # вызван в отношении экземпляра класса, распаковка не нужна так как список
            self.__color = color            # circle1.set_color([55, 66, 77])
        else:
            # print(f'{color} не может быть изменен, должен быть список (R, G, B) в интервале 0-255')
            return self.__color

# Зачем нужен `self`в self.__is_valid_color(color):
# 1. **Доступ к атрибутам и методам объекта:** Когда вы хотите обратиться к атрибутам (например, `self.__color`)
# или методам класса (например, `self.__is_valid_color(color)`) изнутри методов класса, вам нужно использовать `self`
# для указания, что вы обращаетесь к атрибутам или методам текущего экземпляра. Это особенно важно в контексте:
# - Различия между локальными переменными и атрибутами экземпляра.
# - Обеспечения доступа к атрибутам и методам, которые принадлежат конкретному объекту.
# 2. **Прозрачность:** Использование `self` делает код более понятным. Читая код, легко понять, что происходит с
# атрибутами и методами конкретного объекта, а не с какими-то статическими значениями.
# ### Почему нельзя писать __is_valid_color(color) без self
# Когда вы пишете `__is_valid_color(color)` без `self`, Python будет искать этот метод в локальном пространстве
# имен функции или метода, поскольку метод `__is_valid_color` не является локальной функцией, вызовет ошибку `NameError`
# Таким образом, `self` нужен для указания, что `__is_valid_color` — это метод данного класса, и он должен быть вызван
# в контексте текущего экземпляра.

# Задание: Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
# положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides_01(self, *args):
        if len(args) == len(self.__sides):
            if all(isinstance(sides, int) and sides > 0 for sides in args):
                return True
        return False

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            if all(isinstance(sides, int) and sides > 0 for sides in args):
                return True
        return False

# НЕ ПРАВИЛЬНО
    # def __is_valid_00(self, *args):
    #     if len(args) == len(self.__sides):
    #         if not any(isinstance(sides, int) and sides > 0 for sides in args):
    #             return False
    #         else:
    #             return True
    #     return False
# Проверка на соответствие:** Если длина совпадает, выполняется проверка всех элементов в `args` с помощью `any()`.
# Здесь происходит интересный момент:
# - `any(...)` вернет `True`, если хотя бы один из элементов соответствует усл. (`isinstance(sides, int) and sides > 0`)
# - Однако метод возвращает `False`, если **нет ни одного** элемента, который является положительным целым числом.
    # Это означает, что если *все* элементы не являются положительными целыми числами, метод вернет `False`.

# НЕ ПРАВИЛЬНО
    # def __is_valid_00(self, *args):
    #     if len(args) == len(self.__sides):
    #         for i in range(len(args)):
    #             if type(args[i]) == int and args[i] > 0:
    #                 return True
    # В вашем коде, если хотя бы одна из сторон в `args` соответствует условиям (т.е., является целым положительным
    # числом), метод возвращает `True` немедленно.
    # - Это означает, что если первая сторона удовлетворяет условиям, метод не проверяет остальные стороны.
    # Таким образом, это может привести к ошибочному `True`, даже если другие стороны не соответствуют требованиям.
    # - В то время как в предыдущем коде выполняется проверка всех сторон в `args` с помощью функции `all`, которая
    # возвращает `True` только если все элементы соответствуют условиям.
# ПРАВИЛЬНО
    def __is_valid_01(self, *args):
        if len(args) == len(self.__sides):
            for i in range(len(args)):
                if not (isinstance(args[i], int) and args[i] > 0):
                    return False
            return True
        return False
# НЕ ПРАВИЛЬНО
# **Проблема с `all(...)`**: В данном контексте `all(...)` используется неправильно. Вызов `all(...)` ожидает
# итерируемый объект (например, список или другой объект, который можно перебрать). Однако, внутри цикла `for` вы
# передаете одно условие как аргумент. Поэтому `all(...)` вернет `True`, только если условие верно для **каждого**
# из элементов, который будет исполнен на каждом шаге цикла. Но так как `args[i]` — это единственное значение, это
# просто эквивалентно условию, которое не является частью функции `all(...)`.
# - **Логика возврата**: Метод вернет `True` при первой же положительной проверке, и не проверит остальные элементы,
# что неправильно. Это приводит к ситуации, когда, если один из аргументов является корректным, метод вернет `True`,
# даже если другие аргументы не соответствуют условиям.
#     def __is_valid_01(self, *args):
#         if len(args) == len(self.__sides):
#             for i in range(len(args)):
#                 if all(isinstance(args[i], int) and args[i] > 0):
#                     return True
#             return False
#         return False

# ЗАДАНИЕ: Метод get_sides должен возвращать значение я атрибута __sides.

    def get_sides(self):
        return self.__sides

# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
# то не изменять, в противном случае - менять.

    def set_sides_01(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
        else:
            self.__sides

# Ошибки нет, но основной вариант предпочтителен - он возвращает текущее значение, менялось или нет, не важно

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):       # распаковываем кортеж cube1.set_sides(5, 3, 12, 4, 5)
                self.__sides = list(new_sides)
        return self.__sides

# Да, вы правильно понимаете.

# 1. В методе `set_color`, который принимает параметр `color: list[int, int, int]`, распаковка не нужна, потому
# что передается уже список. Когда вы вызываете `circle1.set_color([55, 66, 77])`, вы передаете список целых чисел,
# и метод ожидает именно список и обрабатывает его без необходимости в распаковке.
# 2. В методе `set_sides`, который описан с использованием `*new_sides`, распаковка нужна, потому что вы передаете
# аргументы переменной длины (которые становятся кортежем в `new_sides`). Когда вы вызываете
# `cube1.set_sides(5, 3, 12, 4, 5)`, все переданные значения (5, 3, 12, 4, 5) собираются в кортеж `new_sides`,
# и для его передачи в метод `__is_valid_sides` используется распаковка `*new_sides`.
# Таким образом, в первом случае вы работаете со списком, и распаковка не требуется, а во втором — с кортежем
# аргументов, и для их передачи в другую функцию распаковка необходима.

# Метод __len__ должен возвращать периметр фигуры.

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус)
    def __radius(self):
        return len(self) / (2 * pi)

    def get_square(self):
        return pi * self.__radius() ** 2


class Triangle(Figure):
    sides_count = 3

# # Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
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


    def get_volume_00(self):
        if all(int(sides) == sum(self.get_sides()) / self.sides_count for sides in self.get_sides()):
            sides = self.get_sides()
            return sides[0] ** 3


painted = Figure([10], [100, 100, 100])
print(painted.get_color())

painted_01 = Figure([10], [500, 100, 100])
print(painted_01.get_color())

circle1 = Circle([10], [200, 200, 100]) # (Цвет, стороны)
print(circle1.get_color())
cube1 = Cube([6],[222, 35, 130])
print(cube1.get_color())

print('Проверка на изменение цветов:')
circle1.set_color([55, 66, 77])# Изменится
print(circle1.get_color())
cube1.set_color([300, 70, 15]) # Не изменится
print(cube1.get_color())

print('Проверка на изменение сторон:')
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print('Проверка периметра и площади (круга)')
print(len(circle1))
print(circle1.get_square())

print('Проверка всего по треугольнику')
trianle1 = Triangle([10, 10, 10], [200, 200, 100])
print(trianle1.get_color())
trianle1.set_color([40, 70, 15])
print(trianle1.get_color())
trianle1.set_sides(5, 5, 5)
print(trianle1.get_sides())
print(trianle1.get_square())

print('Проверка объёма (куба):')
print(cube1.all_equal())
print(cube1.get_volume())

print('Testing_01')
d = 15
def __radius():
    from math import pi
    radius = d / (2 * pi)
    return radius

print(__radius())

from math import pi, sqrt

print('Testing_02 - вариант с одним подчеркиванием _sides, не надо получить значение сторон через публичный get_sides')
# есть третий вариант решения задачи с использованием конструктора с кортежами
class Figure:
    sides_count = 0

    def __init__(self, __sides: list[int], __color: list[int, int, int], filled: bool = True):
        if len(__sides) == self.sides_count:
            self._sides = __sides  # Используем одно подчеркивание
        else:
            self._sides = [__sides[0]] * self.sides_count
        self.__color = self.__is_valid_color(__color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color: list[int, int, int]):
        if isinstance(color, list) and len(color) == 3:
            if all(isinstance(c, int) and 0 <= c <= 255 for c in color):
                return color
        return None

    def set_color(self, color: list[int, int, int]):
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            if all(isinstance(sides, int) and sides > 0 for sides in args):
                return True
        return False

    def get_sides(self):
        return self._sides  # Используем одно подчеркивание

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)
        return self._sides

    def __len__(self):
        return sum(self._sides)  # Используем одно подчеркивание

class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return len(self) / (2 * pi)

    def get_square(self):
        return pi * self.__radius() ** 2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        return sqrt(p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2]))  # Формула Герона

class Cube(Figure):
    sides_count = 12


# Примеры создания фигур
painted = Figure([10], [100, 100, 100])
print(painted.get_color())

circle1 = Circle([10], [200, 200, 100])  # (Цвет, стороны)
print(circle1.get_color())

cube1 = Cube([6], [222, 35, 130])
print(cube1.get_color())

print('Проверка на изменение цветов:')
circle1.set_color([55, 66, 77])  # Изменится
print(circle1.get_color())
cube1.set_color([300, 70, 15])  # Не изменится
print(cube1.get_color())

print('Проверка на изменение сторон:')
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

print('Проверка периметра (круга), это и есть длина:')
print(len(circle1))
print(circle1.get_square())

print('Исправленный вызов создания Triangle с тремя сторонами')
triangle1 = Triangle([5, 5, 5], [200, 200, 100])  # Передаем три стороны
print(triangle1.get_color())

# Проверка метода get_square для треугольника
print(triangle1.get_square())