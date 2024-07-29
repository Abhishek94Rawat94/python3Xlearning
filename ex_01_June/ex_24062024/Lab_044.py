# Recursion Concept
# Recursion is a programming technique where a
# function call itself to solve the problem

# Key concept
# Base case
# Recursive case

# Factorial
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(9))
