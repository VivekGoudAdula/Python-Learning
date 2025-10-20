# REGULAR EXPRESSIONS
# RegEx is a sequence of characters that forms a search pattern.

import re
txt = "I study at Aurora deemed University, I am learning Python."


# re.search() function
a = re.search("^I.*University$",txt) # To Search if the string starts with I and ends with University
print(a)

# re.findall() function
b = re.findall("y", txt) # To find all occurrences of y in the string
print(b)

# re.split() function
c = re.split(" ",txt) # To split the string at each space
print(c)

# re.sub() function
d = re.sub("Python","Data Science", txt) # To replace Python with Data Science
print(d)


