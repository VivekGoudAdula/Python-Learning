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

# ---------------------------------

# JOINING SETS
set1 = {"apple", "ball", "cat"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # Merges set1 and set2

set4 = {"dog", "elephant"}
set5 = {"cat", "fox"}
set4.update(set5) # Merges set5 into set4

# INTERSECTION
fruits = {"apple", "banana", "cherry"}
companies = {"microsoft", "apple", "google"}
new = fruits.intersection(companies)
print(new) # Returns items present in both sets

# DIFFERENCE
new = fruits.difference(companies) # Items in fruits but not in companies   

# ---------------------------------

# FROZEN SET

a = frozenset({1,2,34}) # Immutable set
print(type(a))
