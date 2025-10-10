# SETS
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

fruits = { "apple", "mango", "banana", "cherry", "apple" , True, 1}
print(fruits) # Duplicates will be removed

print(len(fruits)) # Length of the set
print(type(fruits)) # Type of the variable

# ---------------------------------

# ACCESSING ITEMS

# Looping through a set
for fruit in fruits:
    print(fruit)

# Checking if an item is in the set
print("banana" in fruits) # Returns True
print("grape" not in fruits) # Returns True

# ---------------------------------

# ADDING ITEMS

fruits.add("orange") # Adding orange

new_fruits = {"kiwi", "pear"}
fruits.update(new_fruits) # Adding multiple items

# ---------------------------------

# REMOVING ITEMS

fruits.remove("banana") # Removes banana, raises an error if not found
fruits.discard("banana") # Removes banana, does not raise an error if not found
fruits.pop() # Removes a random item
fruits.clear() # Empties the set
del fruits # Deletes the set entirely
