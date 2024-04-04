'''
Finds if a number is even. Checking for performance using bitwise operator
'''

from timeit import timeit

def odd_normal(number):
    return number % 2 == 0

def even_bitwise(number):
    return number & 1


normal_time = timeit("odd_normal(5)",number = 100000, globals=globals())
bitwise_time = timeit("even_bitwise(5)",number = 100000, globals=globals())

print(f'{normal_time=}')
print(f'{bitwise_time=}')

print(f'ratio: {normal_time/bitwise_time}')