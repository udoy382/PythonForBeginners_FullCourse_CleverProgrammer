# Understanding For Loops in Python


fruits = ['apple', 'mango', 'orange', 'papaya', 'watermelon']

# print('fruit: ', fruits[0], 0)
# print('fruit: ', fruits[1], 1)
# print('fruit: ', fruits[2], 2)
# print('fruit: ', fruits[3], 3)
# print('fruit: ', fruits[4], 4)


# fruits.append('apple')


"""
i = 0
for fruit in fruits:
    print('fruit:', fruit, i)
    i += 1
"""

"""
for index, fruit in enumerate(fruits):
    print('fruit: ', fruit, index)
"""

"""
for number in [1, 2, 3, 4, 5]:
    print(number)
"""

"""
for _ in range(5): # underscore _ means scpae for loop name its not import to call
    print("haa")
"""

# add 10 apples to the fruits list ~
"""
for _ in range(10):
    fruits.append("Apple")

print(fruits)
"""