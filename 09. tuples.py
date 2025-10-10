# TUPLES
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.

colors = ("red", "green", "blue", "yellow", "green")

print(len(colors)) # Length of the tuple
print(type(colors)) # Type of the variable

# ---------------------------------
# ACCESSING ITEMS
print(colors[0]) # Accessing first item
print(colors[-2]) # Accessing second last item
print(colors[1:4]) # From index 1 to 3
print("blue" in colors) # Checks if blue is in colors and returns True  

# ---------------------------------

# IMMUTABILITY
# colors[1] = "black" # This will raise an error because tuples are immutable

# ---------------------------------

# LOOPING THROUGH A TUPLE
for color in range(len(colors)):
    print(colors[color])

i=0
while i<len(colors):
    print(colors[i])
    i+=1

# ---------------------------------

# JOINING TUPLES
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2

# --------------------------------