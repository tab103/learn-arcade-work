"""
Python variables are dynamic, case-sensitive, must begin with an underscore or letter, but may contain numbers. Simply
put, they "hold" data. This data may be of any form even some you might not expect but most are like other languages.
Python supports floats, integers, booleans, and strings for common data types. See below for examples:
"""

var_one = 10    # integer
var_two = 20.5  # floating point
result = var_one + var_two # add them together, result will be floating point
print(result)

var1 = var_one
var_one = 'oops i just lost the value but I saved it in var1'
print(var_one, var1)

# note this is different
print('var_one')

# by convention, Python prefers variables with underscores but camel case is ok
# spaces in variable names are a bad idea!
# this is a variable = 5 this will cause an error

# by convention, contants are in all caps, not required but proper.
PI = 3.14159



