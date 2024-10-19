# What are List Comprehensions


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# filter and given only EVEN numbers ~
print([number for number in numbers if number % 2 == 0])


# map - double Comprehensions ~
print([number * 2 for number in numbers ])


# get odd number ~
print([odd_number for odd_number in numbers if odd_number % 2 != 0])


# give me all of the odd nubmers CUBES ~
print([x ** 3 for x in numbers if x % 2 != 0])


# SPECIAL BUILT-IN FUNCTIONS with Python ~
"""
>>> sum([1, 2, 3])
6
>>> len([1, 2, 3])
3
>>> max([1, 2, 3, 10, 5, 7])
10
>>> min([1, 50, -7, 337])
-7
"""