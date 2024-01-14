class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __pos__(self):
        return Point(self.x, self.y)
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def negative(self):
        return Point(-self.x, -self.y)
    
    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other: 'Point'):
        self.x += other.x
        self.y += other.y
        return self
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __bool__(self):
        return self.x != 0 or self.y != 0



# p1 = Point(2, 3)
# p2 = Point(2, 3)
# print(id(p1))
# p1 = p1 + p2
# print(id(p1))

# p1 = Point(2, 3)
# p2 = Point(2, 3)
# print(id(p1))
# p1 += p2
# print(id(p1))
    
# p1 = Point(2, 3)
# p2 = Point(2, 3)
# print(p1 == p2)

# # abs(x)
# __abs__

# # round(x)
# __round__

# # floor(x)
# __floor__

# # ceil(x)
# __ceil__

# # x + y
# __add__


# # x * y
# __mul__(self, other)

# # x // y
# __floordiv__(self, other)

# # x / y
# __truediv__(self, other)

# # x % y
# __mod__(self, other)

# # x ** y
# __pow__(self, other)

# # x & y
# __and__(self, other)


# # x < y
# __lt__(self, other)

# # x <= y
# __le__(self, other)

# # x > y
# __gt__(self, other)

# # x >= y
# __ge__(self, other)

# # x == y
# __eq__(self, other)

# # x != y
# __ne__(self, other)


# __int__(self)

# __float__(self)

# __bool__(self)
    
# __complex__(self)

# __str__(self)
    

print([Point(2, 3), Point(1, 2)])
