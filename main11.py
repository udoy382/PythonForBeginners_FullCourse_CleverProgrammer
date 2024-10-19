# Understanding Higher Order Functions in Python


# >>> map
# >>> filter



"""
'''
>>> double([1, 2, 3])
[2, 4, 6]
'''

def double(number):
    return number * 2

# print(double(1))

# print(list(map(double, [1, 2, 3])))

print(list(map(lambda num: num * 2, [4, 5, 6])))
print(list(map(lambda num: num ** 2, [4, 5, 6])))
"""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(list(filter(lambda number: number % 2 == 0, numbers)))