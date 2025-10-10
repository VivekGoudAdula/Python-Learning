# LISTS
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets [] and items are separated by commas.
# Lists are mutable, meaning you can change their content without changing their identity.

groceries = ["Bread", "Milk", "Eggs", "Bread", 10]

print(len(groceries)) # Length of the list
print(type(groceries)) # Type of the variable


# ---------------------------------

# ACCESSING ITEMS
print(groceries[0]) # Accessing first item
print(groceries[2]) # Accessing third item

# NEGATIVE INDEXING
print(groceries[-1]) # Accessing last item

# RANGE OF INDEXES
print(groceries[1:3]) # From index 1 to 2

# ---------------------------------

# MODIFYING ITEMS
groceries[1]="Cheese"  # Changing second item to Cheese
groceries[2:4]=["Butter", "Yogurt"] # Changing items at index 2 and 3

groceries.insert(1,"Mayonnaise") # Inserting Mayonnaise at index 1

# ADDING ITEMS
groceries.append("Juice") # Adding Juice at the end

# ---------------------------------

# REMOVING ITEMS
groceries.remove("Bread") # Removes first occurrence of Bread
groceries.pop(1) # Removes item at index 1
del groceries[2] # Deletes item at index 2
groceries.clear() # Clears the entire list

# ---------------------------------

# LOOPING THROUGH A LIST
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ---------------------------------

# SORTING A LIST
groceries = ["Bread", "Milk", "Eggs", "Bread", 10]
groceries.sort() # Sorts the list in ascending order
groceries.sort(reverse = True) # Sorts the list in descending order
groceries.reverse() # Reverses the order of the list

# ---------------------------------