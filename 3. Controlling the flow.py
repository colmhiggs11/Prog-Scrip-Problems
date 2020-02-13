# Colm Higgins
# Program to ask user to enter an integer and perform calculations 
# based on whether that integer is even or odd.

x = int (input ("Please enter a positive integer"))
while x <= 1:
    if x % 2 == 0:
        print(x)