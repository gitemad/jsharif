# # positional arguments (required arguments)
# def print_bill_item(item, cost):
#     print(f'{item}: {cost}$')

# # print_bill_item('Mobile', 1499)
# print_bill_item(1499, 'Mobile')

# # keyword argument
# def print_bill_item(item, fee, num):
#     print(f'{item}: {fee * num}$')

# print_bill_item(fee=10, item='Cheese', num=2)
# print_bill_item('Cheese', num=2, fee=10)
# print_bill_item('sad', fee=10, 5)


# default parameter
# def print_bill_item(item, fee, num=1):
#     print(f'{item}: {fee * num}$')

# print_bill_item(fee=10, item='Cheese', num=2)
# print_bill_item('Cheese', 10)

# def f(my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append('***')
#     print(id(my_list))
#     print(my_list)

# f()
# f()
# f(my_list=[1, 2, 3])
# f()

# def f(s_in):
#     print('inside', s_in, id(s_in))
#     s_in += 'b'
#     print('inside', s_in, id(s_in))

# s_out = 'a'
# print('outside', s_out, id(s_out))
# f(s_out)
# print('outside', s_out, id(s_out))

# def f(s_in):
#     print('inside', s_in, id(s_in))
#     s_in = [1, 2]
#     print('inside', s_in, id(s_in))

# s_out = [1]
# print('outside', s_out, id(s_out))
# f(s_out)
# print('outside', s_out, id(s_out))

# def sqrt(n):
#     return n ** 0.5

# def f():
#     return 1, 2, 3

# def sum(*numbers):
#     s = 0
#     for n in numbers:
#         s += n
#     return s

# print(sum(1))
# print(sum(1, 2, 3))
# print(sum(1, 2, 3, 4, 5))

# def f(**kwargs):
#     for key, val in kwargs.items():
#         print(key, '->', val)

# def area(
#         r: {
#             'desc': 'radius of circle',
#             'type': float
#         }) -> {
#             'desc': 'area of circle',
#             'type': float
#         }:
#     return 3.141592 * r ** 2

# print(area.__annotations__)

numbers = range(5)
print(list(map(lambda x: x ** 2, numbers)))
