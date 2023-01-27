"""It is helpful to recognize that the code after a function call does not execute until the function
called completes. See examples below

Before you run the code below, what do you think it will print out?
"""

def third_function():
    return " third"

def second_function():
    return " second" + third_function()

def first_function():
    return " first" + second_function()

print(first_function())