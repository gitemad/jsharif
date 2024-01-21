# class Point:

#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     def get_x(self):
#         return self._x
    
#     def set_x(self, value):
#         self._x = value
    
#     def get_y(self):
#         return self._y
    
#     def set_y(self, value):
#         self._y = value

# p = Point(2, 3)
# print(p.get_x())
# print(p.set_x(5))
# print(p.get_x())
# print(p._x) # Bad practice


# class Circle:

#     def __init__(self, radius):
#         self._radius = radius
    
#     def _get_radius(self):
#         return self._radius
    
#     def _set_radius(self, value):
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError
    
#     def _del_radius(self):
#         del self._radius
    
#     radius = property(
#         fget=_get_radius,
#         fset=_set_radius,
#         fdel=_del_radius,
#         doc="The radius property"
#     )

# c = Circle(5)
# c.radius = -10
# print(c.radius)


# class Circle:

#     def __init__(self, radius):
#         self._radius = radius
    
#     @property
#     def radius(self):
#         '''The radius property'''
#         return self._radius
    
#     @radius.setter
#     def radius(self, value):
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError
    
#     @radius.deleter
#     def radius(self):
#         del self._radius


# c = Circle(4)
# print(c.radius)
# c.radius = 10
# print(c.radius)
# c.radius = -6


# class Point:

#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     @property
#     def x(self):
#         return self._x
    
#     @property
#     def y(self):
#         return self._y
    
# p = Point(2, 3)

# p.x = 33
# print(p.x)


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height

r = Rectangle(2, 3)
print(r.area)
r.area = 10