"""
This file has examples of basic printing to the screen with Python.
Note that this prints to the console, not any graphics window created
with the arcade library. Printing to the console is helpful for debugging
or verifying algorithms as well as console applications/scripts.
"""

"""
the simplest of all programs and usually the first one you want to get 
working is a "Hello World" program. Essentially, while very simple these
are still useful to verify your environment is working. For Python, it
shows the the paths to your interpreter are valid. 
"""
# Hello World
print("Hello World") # that's it. running this will print Hello World to the screen.
"""
A couple things to point out that are useful in general. The print() statement is a
Python function. Functions have names, may take arguments, and may return values.
You can write your own functions or you can "call" functions in the standard library
or a library you import into your code. print() is in the standard library. It takes
an argument between the () that specifies what will be printed. In this case we are
printing a "string" which is a sequence of characters. A string is denoted by being
enclosed by either double or single quotes. For example:
"""
print('Hello World') # this does the same thing
"""
So why both? Great question. Sometimes when you are printing out text you may want to
print out single or double quotes within the text. Python needs to be able to distinguish
between the quotes the denote the strings contents and the quotes that are part of the
string. For example: print("The policeman said "Stop"") will not work because it is 
what compilers/interpreters call ambiguous. It can't tell whether the quotes are part
of the string or denote the limits of it. How to fix? You can use single quotes to denote the string and double quotes inside of it
"""
print('The policeman said "Stop"')
"""
And yes you can reverse this if you want to include an apostrophe in your string:
"""
print("The criminal's gun was later found in the alley.")

"""
What if you don't know ahead of time or you have a combination of both? The generic 
solution is to use an "escape" character which is the \ character. It basically
tells the Python interpreter to "treat the next character literally, don't make it
special. In this way you can:
"""
print("The criminal said \"That\'s not mine\" when he saw the gun")

"""
This always works and, in fact there are other escape sequences of interest beside
single and double quotes

\t is a tab character
\r is a carriage return (you won't use this much)
\n this is a carriage return and a line feed. It basically bumps the output to the next line
"""
print("The words \none\ntwo and\nthree are all on separate lines.")

"""
Also, the triple-quotes that are used in this document are not just for comments,
you can use them for printing out multiple lines of text also like this:
"""
print("""Contrary to popular belief, Lorem Ipsum is not simply random text.
It has roots in a piece of classical Latin literature from 45 BC, making it
over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney
College in Virginia, looked up one of the more obscure Latin words, consectetur,
from a Lorem Ipsum passage, and going through the cites of the word in classical
literature, discovered the undoubtable source. Lorem Ipsum comes from sections
1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and
Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics,
very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor
sit amet..", comes from a line in section 1.10.32.""")

"""
Suppose I want to print out numbers? It's easy but remember anything in quotes is
interpreted by Python as a string, even numbers. Also, when you use the + symbol
with strings, it concatenates them together (i.e. adds). For example
"""
print("3" + "5") #will print out 35 but
print(3 + 5) # will print out 8, Python will add the 2 numbers together before printing
print("The answer is " + "5") # this will print out the answer is 5
# or
print("The answer is " + str(6)) # str converts a number to a string
"""
If you want to print out a number of things at once, you can separate them by commas:
"""
print("The answer is",6,"or maybe it is",10) # Python will put a single space between elements being printed

"""
Finally, by default Python prints and the advances to the next line. If you wanted to
keep the output on the same line, you can change the end character like this:
"""

print("The answer is",42,end="")
print(" And this is on the same line!")

"""
That's good for basic printing, we'll look at formatted printing in the future.
"""