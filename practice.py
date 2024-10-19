# Practice Lists and Loops


# Lists & loops ==>>


"""
'''
double([1, 2, 3, 4, 5])
>>> [2, 4, 6, 8, 10]
'''

def double(numbers: list):
    result = []
    for number in numbers:
        result.append(number * 2)
    
    return result


print(double([1, 2, 3, 4, 5]))
"""


"""
'''
Count words if given a string, should count &
return the number of words

>>> count_words('Hi my name is Udoy)
5
'''

def count_words(phrase: str):
    return len(phrase.split())
    

print(count_words("Hi my name is Udoy and I love Sara"))
"""


"""
def double(numbers: list):
    result = []
    for number in numbers:
        result.append(number * 2)
    
    return result


print(double([1, 2, 3, 4, 5]))
"""


"""
'''
>>> sum_list([1, 2, 3])
6
'''

from functools import reduce

def sum_list(numbers: list):
    result = reduce(lambda a, b: a + b, numbers)
    print(result)

sum_list([1, 2, 3])
"""


# Another way to sum of some numbers ~
"""
def sum_list(numbers: list):
    count = 0
    
    for number in numbers:
        count += number

    return count

print(sum_list([1, 2, 3]))
"""


# We do this same sum_list in manually ~
"""
count = 0
numbers = [1, 2, 3, 4]
count += numbers[0]
count += numbers[1]
count += numbers[2]
count += numbers[3]
print(count)
"""


"""
'''
>>> find_max([1, 5, 10, 3])
10
'''

def find_max(numbers: list):
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max

print(find_max([1, 5, 10, 3, 44, 436, 2, 2, 1]))
"""