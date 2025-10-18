# RANGE
# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
# This set of numbers has its own data type called range.
# SYNTAX: range(start, stop, step)

a = range(10)
print(type(a)) # OUTPUT: <class 'range'>

x = range(10) # STOP
y = range(3,7) # START , STOP
z = range(1,10,2) # START , STOP , STEP
print(list(x))
print(list(y))
print(list(z))

# --------------------------------------------------

# USING RANGES
# range() is often used with for loop
for i in range(10):
    print(i)

# --------------------------------------------------

# SLICING RANGES
# Like other sequences, ranges can be sliced to extract a subsequence.

x = range(10)
print(x[2])
print(x[:5])

# --------------------------------------------------

# MEMBERSHIP TESTING
# Ranges support membership testing with the in operator.

b = range(40)
print(39 in b)
print(69 in b)

# --------------------------------------------------

# LENGTH
# Ranges support the len() function to get the number of elements in the range.

c = range(22)
print(len(c))

# --------------------------------------------------