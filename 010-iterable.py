# # class Counter:

# #     def __init__(self, max=0):
# #         self.max = max
    
# #     def __iter__(self):
# #         self.n = 0
# #         return self
    
# #     def __next__(self):
# #         if self.n <= self.max:
# #             result = 2 ** self.n
# #             self.n += 1
# #             return result
        
# #         raise StopIteration

# # # numbers = Counter(5)
# # # iterator = iter(numbers)

# # # print(next(iterator))
# # # print(next(iterator))
# # # print(next(iterator))
# # # print(next(iterator))
# # # print(next(iterator))
# # # print(next(iterator))

# # for i in Counter(5):
# #     print(i)


# class InfOddIter:

#     def __iter__(self):
#         self.num = 1
#         return self
    
#     def __next__(self):
#         num = self.num
#         self.num += 2
#         return num

# odds = iter(InfOddIter())
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))


class FunctionalList:

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values
    
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        return self.values[key]
    
    def __setitem__(self, key, value):
        self.values[key] = value
    
    def __delitem__(self, key):
        del self.values[key]
    
    def __iter__(self):
        return iter(self.values)
    
    def __reversed__(self):
        self.values = self.values[::-1]
        return self
    
    def __str__(self):
        return str(self.values)
    
    def __repr__(self):
        return repr(self.values)

lst = FunctionalList([1, 2, 3])
# print(len(lst))
print(lst[0])
lst[1] = 20
del lst[1]
print(lst[1])
print(reversed(lst))