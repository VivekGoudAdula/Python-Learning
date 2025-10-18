# RECURSION
# Recursion is when a function calls itself

def count(n):
    if n <=0:
        print("DONE")
    else:
        print(n)
        count(n-1)
count(5)

# ---------------------------------------------

# BASE CASE AND RECURSIVE CASE
# Every recursive function must have two parts:
        # A base case - A condition that stops the recursion
        # A recursive case - The function calling itself with a modified argument

# FACTORIAL
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

# FIBONACCI SEQUENCE
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))

# TO FIND MAXIMU VALUE IN A LIST
def max(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        max_of_rest = max(numbers[1:])
        return numbers[0] if numbers[0]> max_of_rest else max_of_rest
list = [4,2,9,8,0,-1]
print(max(list))