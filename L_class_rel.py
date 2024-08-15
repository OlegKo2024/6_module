class Human:
    head = True


class Student(Human):

    def about(self):
        print('I am student')

human = Human()             # создали объект класса Human
student = Student()         # создали объект класса Student

print(human.head)           # получил значение - True
student.about()             # вызвал метод - I am student

print('Не связаны пока student c Human - связываю')
# class Student: - было
# class Student(Human): - стало

print(student.head)         # True
student.head = False
print(student.head)         # # False

print('Как в родительском связаться c Student типа human.about')
# используем __init__

class Human:
    head = True

    def __init__(self):
        self.about()

class Student(Human):
    head = False

    def about(self):
        print('I am student')


# human = Human()             # создали объект класса Human
student = Student()
print(student.head)
"""
не вызывал метод about, но получил I am student и
False (что ожидаемо). Но как с I am student?
- создаем объект-экземпляр дочернего класса student = Student()
- по class Student(Human): идет обращение к родителю - class Human
- срабатывает __init__ по отношению к student
- в __init__ по self и далее self.about(), 
- что и запускает метод about"""

print("student и teacher имеют одинаковый метод - принцип DRY - DO NOT REPEAT YOURSELF")
"""
И student и teacher имеют одного родителя
поэтому вместо дублирования метода, мы можем перенести его в родительский класс"""
class Human:
    head = True

    def say_hi(self):
        print('Hi')

class Student(Human):
    head = False

    def about(self):
        print('I am student')

class Teacher(Human):       # который также может здороваться
    pass



student = Student()
teacher = Teacher()

student.say_hi()            # Hi
teacher.say_hi()            # Hi - работает

"""
Вывод:
изначально ссылаемся на пространство имен класса, ищем и пытаемся вызвать метод или атрибут
не найдя, мы ищем и пытаемся вызвать метод или атрибут в родительском классе
найдя используем его.
Мы увидели:
- можем получить значение атрибута от родителя
- можем запустить метод не указывая его явно, через _init__ и найдя ссылку на него там
- можем запустить метод, указанный к родительском классе, вызывая его через по объекту в дочернем классе(ах)
"""