# Colm Higgins
# This program will read in a .txt file and count 
# the number of chosen characters in that file.

# Inputs take in the required filepath & character wanted to search in file
x = input("Enter directory of file\n")
y = input("\nEnter an upper/lowercase letter and\nI'll tell you how many times its used!! \n")

# Opens & reads the file as f, searches for variable y and counts the times used.
# Using the with statement allows for less code and will 
# automatically close the file when program has run.
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
with open(x,'r') as f:
    print("The letter {} is used".format(y),f.read().count(y),"times")