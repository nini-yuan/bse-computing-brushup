#
# You can take a look at the tests in
# "test_exercises.py", but you do not need to
# change anything there.
#
# See the README for how to run the tests.


#
# 1)
# Create a function named "triple" that
# takes one parameter, x, and returns the
# value of x multiplied by three.
#
def triple(x):
    return x*3

#
# 2)
# Create a function named "subtract" that
# takes two parameters and returns the first
# value minus the second.
#
def subtract(x, y):
    return x-y

#
# 3)
# Create a function named "safe_subtract" that
# takes two parameters and returns the first
# value minus the second.
# If the two values cannot be subtracted, it
# returns None instead.
#
# HINT: you could check the types of the values
# before subtracting them. (There is also a neater
# way to do this, using try/except, which we will
# see later.)
#
def safe_subtract(x,y):
    try:
        return x-y
    except TypeError:
        return None
#
# 4)
# Create a function named "greet_person". It should
# accept a string as an argument and return that
# string as part of a longer sentence that says hello:
# e.g. "Anastasiia" --> "Hello, Anastasiia!"
# If the function is called with an argument that is
# not a string, it should return "Please provide a name."
# e.g. 5 --> "Please provide a name."
#
def greet_person(string):
    try:
        return "Hello, " + string + "!"
    except TypeError:
        return "Please provide a name."