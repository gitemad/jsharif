## Single Leading Underscore (_var)
# import module

# print(module._internal_func())


## Single Trailing Underscore (var_)
# def make_object(name, class_):
#     pass

## Double Leading Underscore (__var)
# class Test:
#     def __init__(self):
#         self.a = 1
#         self._b = 2
#         self.__c = 3
    
#     def __method(self):
#         return 'test method'

# class ExtendedTest(Test):

#     def __init__(self):
#         super().__init__()
#         self.a = 'overridden'
#         self._b = 'overridden'
#         self.__c = 'overridden'

#     def __method(self):
#         return 'extended test method'
# t = ExtendedTest()
# print(t.a)
# print(t._b)
# print(t._Test__method())
# print(t._ExtendedTest__method())


# Double Leading and Trailing Underscore (__var__)
# magic method

# Single Underscore (_)

for _ in range(5):
    print('hello')

name, age, _ = ('Emad', 26, 'jhsdj')

1_000_000_000
1000000000