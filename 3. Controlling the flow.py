# Colm Higgins
# Program to ask user to input an integer and perform set calculations 
# based on whether that integer is even or odd.

# Asks user to input an positive integer.
b = int (input ("Please enter a positive integer:\n"))
# Assigning values to the variables for the set calculations 
d = 2
m = 3

# Loop will run until it reaches 1. **Don't put in >= 1 or it will create infinte loop.
# If numbers is even first calculation is run, if odd second calculation.
# This runs until the value of "b" is 1.
# While loop research from "A Whirlwind Tour of Python, Jake VanderPlas"
# Also https://docs.python.org/3/tutorial/controlflow.html?highlight=control
while b > 1:
    # Any number is even if after dividing by two there is no
    # remainder left over.
    if b % d == 0:
        # If integer is even it will be divided by two until it
        # reaches an odd integer.
        b = b/d
    # If remainder is not equal to zero when divided by two then integer is odd.
    elif b % d != 0:
        # If integer is odd it will be multiplied by 3 and 1 added to this answer.
        b = (b*m)+1
    print(b)
