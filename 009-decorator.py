# def parent():
#     def first_child():
#         print('Printing from first child')

#     def second_child():
#         print('Printing from second child')
    
#     print('Printing from parent function')

#     second_child()
#     first_child()

# parent()

# def parent(num):
#     def first_child():
#         return 'first child'

#     def second_child():
#         return 'second child'
    
#     if num == 1:
#         return first_child
    
#     return second_child

# # print(parent(1)()) # parent(1) -> first_child

# child = parent(1)
# print(child())

# def my_decorator(func):
#     def wrapper():
#         print('before calling func')
#         func()
#         print('after calling func')
    
#     return wrapper

# @my_decorator
# def say_hi():
#     print('Hi!')

# def say_hello():
#     print('Hello!')

# # say_hi = my_decorator(say_hi)
# # say_hi()

# say_hi()


# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         output = func(*args, **kwargs)
#         return output
    
#     return wrapper

# # @do_twice
# # def greet(name):
# #     print(f'Hello {name}')

# # greet('Emad')

# @do_twice
# def return_greeting(name):
#     print('at greeting function')
#     return f'Hi {name}'

# output = return_greeting('Emad')
# print(output)

def bold_text(func):
    def wrapper(*args, **kwargs):
        return f'<b>{func()}</b>'
    
    return wrapper

@bold_text
def get_name():
    return 'Emad'

print(get_name())