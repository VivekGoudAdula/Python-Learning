a= 10
b = 20

# ARITHMETIC OPERATORS

print(a + b) # Addition
print(b - a) # Subtraction
print(a * b) # Multiplication
print(b / a) # Division
print(b % a) # Modulus
print(a ** 2) # Exponentiation
print(b // a) # Floor division

# --------------------------------

# ASSIGNMENT OPERATORS
c = a + b # c is 30
c += a # c = c + a, c is 40
c -= a # c = c - a, c is 30
c *= a # c = c * a, c is 300
c /= a # c = c / a, c is 30.0
c %= a # c = c % a, c is 0.0
c **= a # c = c ** a, c is 0.0
c //= a # c = c // a, c is 0.0

# --------------------------------

# COMPARISON OPERATORS
print(a==b) # Equal to, False
print(a!=b) # Not equal to, True
print(a>b) # Greater than, False
print(a<b) # Less than, True
print(a>=b) # Greater than or equal to, False
print(a<=b) # Less than or equal to, True

# --------------------------------

# LOGICAL OPERATORS

x = 5
print(a>2 and x<10) # AND, True
print(a>2 or x>10) # OR, True
print(not(a>2 and x<10)) # NOT, False

# --------------------------------

# IDENTITY OPERATORS

print(a is b) # is, False
print(a is not b) # is not, True

# --------------------------------

# MEMBERSHIP OPERATORS

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # in, True
print("orange" not in fruits) # not in, True

# -------------------------------