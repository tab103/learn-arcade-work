# iterative algorithm to calculate the factorial of a
def factorial(a):
    total = 1
    for i in range(a,1,-1):
        total *= i
    return total

print(factorial(5))