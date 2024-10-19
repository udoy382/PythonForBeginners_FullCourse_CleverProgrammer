# What are Dictionaries in Python


# KEY VALUE PAIRS ~

"""
person = {'name': 'Udoy', 'shirt': 'Black', 'laptop': 'HP'}

# print(person)
print(person['name'])
print(person['shirt'])
print(person['laptop'])
"""


def introducer():
    person2 = {
        'name': 'Sara',
        'age': 14,
        'class': 'Ten',
        'favorite color': 'Black',
        'dream': 'Robotic Enginner',
        'assets': 100,
        'debt': 50,
        'favoriteFruits': ['apple', 'banana', 'mango', 'ornage'],
        'netWorth': lambda: person2['assets'] - person2['debt']
    }

    # Assign or Update the dictonary values ~
    person2['address'] = "Habiganj"
    person2['favoriteTechnology'] = ['Phone', "Laptop", "VR Box"]
    person2['assets'] = 1000

    # Print this dictonary ~
    print(f"Hi! my name is {person2['name']}, I am {person2['age']} years old and I am currently studying in class {person2['class']}.\n My favorite color is {person2['favorite color']} and I want to become a {person2['dream']} in future.\n My netWorth is ${person2['netWorth']()}. My favorite fruits is {person2['favoriteFruits']} I live in {person2['address']} I love technology like {person2['favoriteTechnology']}")

    # Print this dictonary `keys` and `values` ~
    # print(person2.keys())
    # print(person2.values())


# Call the functions here~
# introducer()


# NOTE:
# >>> Mutable (change-able)
# >>> Immutable (unchange-able)
# >>> Dictionary is the `mutable`
# >>> Tuple is the immutable. It cannot change


# -----------------What are even Tuple in Python-----------------

numbers = (1, 2)
# print(numbers)
# print(type(numbers))
# print(numbers[0])


# 'tuple' object does not support item assignment
numbers[0] = 11
# print(numbers)