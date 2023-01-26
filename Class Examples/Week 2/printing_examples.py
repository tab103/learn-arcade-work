import math

"""
First, lets do some comments. Triple quotes denote a multi-line comment like this. It can also be used to
capture multiline strings for printing.

Single line comments start with a # and go to the end of the line

Note that printing can also be used to print to a file. However, it won't print to a graphics window automatically 
have to use library methods to render text on the screen.

However, printing with an arcade program will work as it goes to the terminal window. Use it for debugging as it is very
handy for that. Just remember that printing to the terminal may slow down your program.
"""
print("This is a message to whoever runs this program!") # Simple print to the screen. By default, it includes a newline
print("To remove the newline (i.e. keep it on the same line.", end='') # this keeps the cursor on the same line
print("Using commas to separate items to be printed","will insert a space between them.")
x = 5
y = 10
z = 15
print(x,y,z) # this prints these variable values to the screen
print(x + y + z) # this prints their sum
print("The sum of x, y, z is ", x + y + z) # same thing with description

# this uses positional arguments, i.e. the 0, 1, and 2 indicate the position of the variables.
print('The value of x is {0} the value of y is {1} and the value of z is {2}'.format(x, y, z))

# this uses a format string, note the lowercase f
print(f'The value of x is {x} the value of y is {y} and the value of z is {z}')

# suppose you want to limit the precision, like with pi. This prints out 1 number to the left and 4 to the right
# of the decimal.
print("The value of pi is approximately equal to %1.4f" % (math.pi))

# scientific notation
print("A gigabit is %10.0E bits " % (1024**3))

# hexadecimal
print("135 in hexadecimal is", hex(135))
# or
print("or 135 in hexadecimal is 0x%02x" % (135))

# binary
print("135 in binary is", bin(135))
# or
print("or 135 in binary is {0:b}".format(135))

# you can also print the result of functions
print("The value of sine at pi/2 radians is ", math.sin(math.pi/2))

# you can add strings together with the + operator
print("To concatenate strings just" + " use the + symbol.")

# another way to add a new line is with the \n character
print("This is line 1\nline2\nline3")

# The \ is the escape character. If you want to print it or a quote you have to escape it
print("Use the escape \\ character to print a quote \"")

# Alternative you can alternate single and double quotes
print('Use a single quote to wrap a string with a double quote (") ')


