# What are Sets in Python


# SETS {} -->> used for getting unique stuff ~

"""
list1 = ['python', 'ruby', 'javascript']
list2 = ['sql', 'ruby', 'javascript', 'c++']

results = list1 + list2
print(results)
print(set(results))
print("python" in results)


x = {1, 2, 3, 2, 2, 5}
y = set([1, 2, 2, 3, 4, 5])


print(y)
# print(type(x))
# print(x)
"""

# SPECIAL KEYWORDS:
# list, len, max, min, set, dict


# ----------------------------------------------------


'''
Create a function unique, that takes in a list
and returns only unique items

>>> unique(['ruby', 'ruby', 'python'])
['ruby', 'python']
'''


def unique():
    list1 = ['ruby', 'ruby', 'python']
    return list(set(list1))

results = unique()
print(results)


unique2 = lambda languages: list(set(languages))
print(unique2(['sql', 'c++', 'c++']))