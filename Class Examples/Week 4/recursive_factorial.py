# recursive function to calculate the factorial of a number
def factorial(a):
    if a == 1:  # terminating condition
        return 1
    else:
        return a * factorial(a - 1) # recursive call

print(factorial(6))