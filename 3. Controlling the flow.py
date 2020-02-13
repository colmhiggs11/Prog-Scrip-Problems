# Colm Higgins
# Program to ask user to enter an integer and perform calculations 
# based on whether that integer is even or odd.

b = int (input ("Please enter a positive integer"))
m = 2

# This loop will print all even numbers from integer input to 1
while b > 1:

    if b % m == 0:
        b = b/m
        
        print (b)
    elif b % m != 0:
        b = (b*3)+1

        print(b)