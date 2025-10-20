# PYTHON NONE
# The None keyword is used to define a null value, or no value at all.

a = None
print(a) # OUTPUT: None

print(type(a)) # OUTPUT: <class 'NoneType'>

# --------------------------------------------------------------------

# COMPARING TO NONE

# is
if a is None:
    print("a is None") # THIS WILL BE THE OUTPUT    
else:
    print("a is not None")

# is not
if a is not None:
    print("a is not None")
else:
    print("a is None") # THIS WILL BE THE OUTPUT

# --------------------------------------------------------------------

# Boolean Value of None
print(bool(None)) # OUTPUT: False

# --------------------------------------------------------------------

# FUNCTION THAT RETURNS NONE
def add(a,b):
    c=a+b
d = add(2,3)
print(d) # OUTPUT: None

# ---------------------------------------------------------------------