# Some simple functions
def return_a_value():
    return "This function returns a value"

def pass_an_argument(s):
    print(s)    # this will print the "message from main"
    print(return_a_value())

""" Simple function definition. The keyword 'def' indicates a function definition. The next token is the name
function followed by parentheses which indicate parameters, if any, that are being passed to the function. After
the closing parentheses, the colon indicates the start of the body of the function. Every line in the body
of the function must be indented the same number of spaces. (Don't do the manually, let the IDE handle the indention.
At the end of the function, you can return something to the caller with an optional return statement.
"""
def main():
    print("I am a simple function!") # prints a simple message
    pass_an_argument("message from main") # call a function from this function and pass a string


"""You will often see this code, and essentially, all you need to know is that the global variable
__name__ will be equal to __main__ if the script being executed is the "top level script" meaning
the script that imports other scripts. This allows you to conditionally run the code only if
it is being directly executed but not if it is being imported.

See also: https://realpython.com/if-name-main-python/#:~:text=Nesting%20code%20under%20if%20__,defined%2C%20but%20no%20code%20executes.
"""
if __name__ == "__main__":
    main()