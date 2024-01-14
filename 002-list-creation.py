## method 1
# squares = []

# print(id(squares))
# for i in range(1, 11):
#     # squares = squares + [i * i] # id changes
#     # squares += [i * i] # id remains
#     squares.append(i * i)
#     # squares.append(i ** 2)

# print(squares)
# print(id(squares))



## method 2
# def square(n):
#     return n ** 2

# numbers = list(range(1, 11))
# squares = map(square, numbers)

# squares_itr = iter(squares)
# print(list(squares_itr))
# print(next(squares_itr))



## method 3
# squares = [i ** 2 for i in range(1, 11)]
# squares = [pow(i, 2) for i in range(1, 11)]
# print(squares)

# sentence = 'the rocket came back from mars'
# vowels = [ch for ch in sentence if ch in 'aeiou']
# vowels = {ch for ch in sentence if ch in 'aeiou'}
# print(vowels)

numbers = [1.25, -4.2, 5, 8, -8, 63, 23, -1.3]
abs_numbers = [n if n >= 0 else -n for n in numbers]

print(abs_numbers)