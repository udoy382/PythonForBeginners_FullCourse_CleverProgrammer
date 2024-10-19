# Getting started with python function


def say_my_name():
    print("Saifur Rahman Udoy")
    print("Sara")
    print("Mitu")
    print("Diba")

# say_my_name()


def say_my_name_2(name):
    print(name)


# say_my_name_2("Udoy")


def greeting(name, greet="Sara"):
    """
    Greeting takes in 2 argumetns, greet & name
    and it greets the user
    """
    print(f"Hey! {greet} {name}")


# Multiple arguments + Default Arguments ~
# greeting("Sara", "Udoy")

# Positional Arguments ~
# greeting("Udoy")

# Named Arguments ~
# greeting( greet="Hi", name="Udoy")


def sum(a, b):
    '''
    Takes 2 integers, returns their sum
    >>> sum(1, 2)
    '''

    return a + b

# print(sum(1, 2))


def calculateFoodTotal(food_amount, tip_percentage):
    tip_amount = food_amount * tip_percentage / 100
    total_amount = food_amount + tip_amount

    return total_amount


# result = calculateFoodTotal(100, 10)
# print(result)

# user = input("How is the weather? > ")
# if user == "sunny":
#     print("😎")
# elif user == "rain":
#     print("☔")
# elif user == "cloudy":
#     print("☁️")
# elif user == "thunderstorm":
#     print("⛈️")
# else:
#     print("Try again")

def weather_to_emoji(user_input: str):
    '''
    weather_to_emoji takes in 1 argument as a string
    (expected inputs: "rain", "thunderstorm", "cloudy", "sunny")

    >>> weather_to_emoji("rain")
    "☔"

    >>> weather_to_emoji("thunderstorm")
    "⛈️"

    >>> weather_to_emoji("sunny")
    "😎"

    >>> weather_to_emoji("cloudy")
    "☁️"
    '''

    if user_input == "sunny":
        print("😎")
    elif user_input == "rain":
        print("☔")
    elif user_input == "cloudy":
        print("☁️")
    elif user_input == "thunderstorm":
        print("⛈️")
    else:
        print("Try again")


weather_to_emoji("thunderstorm")


# Exercise 1 ==>>

def bigger_guy(x, y):
    """
    This function bigger_guy takes in two
    numbers and returns the bigger one.

    >>> bigger_guy(2, 3)
    """

    # Method 1 ~
    """
    a = max(x, y)
    return a
    """

    # Method 2 ~
    if x > y:
        return x
    else:
        return y


result = bigger_guy(90, 300)
print(result)
