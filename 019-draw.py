import random

students = [
    'زین الله مظفری',
    'مهسا صادقیان',
    'مبینا هاشمی',
    'امیر جاسمی',
    'مجتبی ابراهیمی',
    'رضا زارعی',
    'سروش پریدخت',
    'آرین مقدم',
    'دریا کوثر',
    'شیما قاسمی کیا',
    'آرزو بنشاسته',
    'مرجان باقیان',
    'رضا یوسفی',
    '',
]

with open('draw.txt', 'w', encoding='utf-8') as file:
    while students:
        group = random.sample(students, 2)
        students.remove(group[0])
        students.remove(group[1])
        random.shuffle(students)
        file.write(str(group))
        file.write('\n')