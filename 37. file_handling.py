# FILE HANDLING
# USING PYTHON WE CAN CREATE, READ, UPDATE, AND DELETE FILES.

# open() FUNCTION 
#The open() function is used to open a file in python
# It takes two parameters: filename and mode

# There are four modes in which a file can be opened:
# 'r' - Read mode which is used to read the contents of a file. (default mode)
# 'w' - Write mode which is used to write data to a file. If the file already exists, it will be overwritten.
# 'a' - Append mode which is used to add data to the end of a file
# 'x' - Create mode which is used to create a new file. If the file already exists, it will raise an error. 

# Example of opening a file in read mode
f = open("demo.txt", "r")  # Open the file demo.txt in read mode
