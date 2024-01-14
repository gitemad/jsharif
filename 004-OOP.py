import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, fill='white', outline='black'):
        self.fill = fill
        self.outline = outline
    
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    sides_count = 4

    def __init__(self, width, height, fill='yellow', outline='black'):
        super().__init__(fill, outline)
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):

    def __init__(self, width, fill='yellow', outline='black'):
        super().__init__(width, width, fill, outline)

class Circle(Shape):

    def __init__(self, radius, fill='white', outline='red'):
        super().__init__(fill, outline)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

s = Square(5)
# print(isinstance(s, Square))
# print(isinstance(s, Rectangle))
# print(isinstance(s, Circle))
# print(isinstance(s, Shape))

print(issubclass(Square, Rectangle))
print(issubclass(Square, Square))
print(issubclass(Rectangle, Square))
print(issubclass(Rectangle, object))

# # rect1 = Rectangle(3, 4, outline='blue')
# # rect2 = Rectangle(5, 5)

# # square = Square(7, 'blue')

# # square.width = 8
# # print(square.width)
# # print(square.height)
    
# circle = Circle(5)
# print(circle.radius)
# print(circle.calculate_area())
# print(circle.outline)


# class Person:

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def move(self):
#         print('Person moved!')

# class FootballPlayer(Person):

#     def __init__(self, first_name, last_name, club):
#         Person.__init__(self, first_name, last_name)
#         self.club = club

#     def move(self):
#         print('FootballPlayer moved!')

# class Student(Person):

#     def __init__(self, first_name, last_name, university):
#         Person.__init__(self, first_name, last_name)
#         self.university = university

#     def move(self):
#         print('Student moved!')

# class FootballPlayerStudent(FootballPlayer, Student):

#     def __init__(self, first_name, last_name, club, university):
#         FootballPlayer.__init__(self, first_name, last_name, club)
#         Student.__init__(self, first_name, last_name, university)

#     def move(self):
#         super(FootballPlayer, self).move()


# fps = FootballPlayerStudent('fname', 'lname', 'club', 'uni')

# fps.move()


# class A:

#     def __init__(self):
#         super().__init__()
#         print('A')

# class B(A):

#     def __init__(self):
#         super().__init__()
#         print('B')

# class C(A):

#     def __init__(self):
#         super().__init__()
#         print('C')

# class D(A):

#     def __init__(self):
#         super().__init__()
#         print('D')

# class E(D, C, B):

#     def __init__(self):
#         # super().__init__()
#         super(D, self).__init__()
#         print('E')

# E()
