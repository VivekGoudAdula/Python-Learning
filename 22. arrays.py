# ARRAYS
# In python Arrays are used to store multiple values in one single variable

cars = ["Volvo", "Audi", "Mercedez", "BMW"]
print(cars)

# --------------------------------------------------

# ACCESSING THE ELEMENTS OF AN ARRAY
print(cars[0]) # OUTPUT: Volvo
print(cars[2]) # OUTPUT: Mercedez

# --------------------------------------------------

# MODIFYING THE ELEMENTS OF AN ARRAY
cars[0] = "Toyota"
print(cars)

# --------------------------------------------------

# LENGTH OF AN ARRAY
print(len(cars))

# --------------------------------------------------

# LOOPING ARRAY ELEMENTS
for car in cars:
    print(car)

# --------------------------------------------------

# ADDING ARRAY ELEMENTS
cars.append("Porsche")
print(cars)

# --------------------------------------------------

# REMOVING ELEMENTS OF AN ARRAY

# pop() method
cars.pop(3)
print(cars)

# remove() method
cars.remove("Porsche")
print(cars)

# --------------------------------------------------

# clear() - to remove all elements from the array

print(cars.clear())