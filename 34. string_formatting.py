# STRING FORMATTING

# f-strings
# Fstrings allow us to format selected parts of a string

txt = f"Hello World"
print(txt)

# --------------------------------------------------------------

# PLACEHOLDERS AND MODIFIERS IN F-STRINGS

# To format values in an f-string we use placeholders, repreented in {}
price = 20.9543
txt = f"Price of the item is {price} inr"
print(txt)

# We can also use format modifiers to format the value inside the placeholder
p = f"Price of the item is {price:.2f} inr" # .2f will format the float value to 2 decimal places
print(p)

# --------------------------------------------------------------

# OPERATIONS IN F-STRINGS
a = 10
b = 20
add = f"Sum of {a} and {b} is {a+b}"
print(add)
mul = f"Multiplication of {a} and {b} is {a*b}"
print(mul)

# if else in f-strings
print(f"{'a is greater than b' if a>b else 'b is greater than a'}")

# --------------------------------------------------------------

# EXECUTE FUNCTIONS IN F-STRINGS

place = 'hyderabad'
txt = f'Welcome to {place.upper()}'
print(txt)