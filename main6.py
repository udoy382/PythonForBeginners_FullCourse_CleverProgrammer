# What are Lists in Python


# LISTS (ARRAYS) ~
fruits = ['apple', 'banana', 'coconat', 'orange', 'stobary']
fruits2 = ['apple', 'banana', 'coconat', 'orange', 'stobary', "Udoy", "Sara", 436, 22.99, True, False]

# print(fruits)
# print(type(fruits))


# Append any values in this list with `append` method ~
fruits.append("papaya")
fruits.append("watermelon")
# print(fruits)


# INDEXING ~
# print(fruits[0])
# print(fruits[1])
# print(fruits[3])


# hwo to ALWAYS get the last item in an array ~

# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])


# SLICING ~

# print(fruits[0:2])
# print(fruits[2:5])
# print(fruits[0:4])
# print(fruits[::2])
# print(fruits[0: len(fruits) -1])
# print("Hi! My name is Udoy"[0: 10])
# print("Hi! My name is Udoy"[-1])
# print(fruits[0:5:1])

# print(len(fruits))


# ----------------------------

# fruits2.clear()
# print(fruits2)

b = fruits2.insert(4, "Love You")
# print(fruits2)

c = fruits2.index("Udoy")
# print(c)

# fruits2.remove("Sara")
# print(fruits2)

# print(fruits2.count("Udoy"))

# fruits2.pop()
# print(fruits2)

# fruits2.reverse()
# print(fruits2)