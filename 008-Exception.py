# num = int(input('Enter numwerator: '))
# den = int(input('Enter denomerator: '))

# person = {'name': 'Emad'}

# try:
#     print(person.age)
#     print(f'{num} / {den} = {num / den}')
# except ZeroDivisionError as e:
#     print(e)
# except AttributeError as e:
#     print(e)
# except:
#     print('Unknown Error')

# def get_dict():
#     return person.age

# try:
#     # print(person.age)
#     print(f'{num} / {den} = {num / den}')
# except Exception as e:
#     print(e)
# else:
#     print('else executed')
# finally:
#     print('finally executed')

# print('##############')

# age = int(input('Enter your age: '))
# if age < 0:
#     raise Exception(f'Age must be postive. The value of age was {age}')

# print('age:', age)


class AgeNotInRangeError(Exception):

    def __init__(self, age, message='age is not in (20, 40) range', *args):
        self.age = age
        self.message = message
        super().__init__(message, *args)

def get_age():
    age = int(input('Enter your age: '))
    if not 20 <= age <= 40:
        raise AgeNotInRangeError(age)
    return age

try:
    age = get_age()
except AgeNotInRangeError as e:
    print(e)