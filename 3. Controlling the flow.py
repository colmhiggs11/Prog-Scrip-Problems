# Colm Higgins
# Program to ask user to enter an integer and perform calculations 
# based on whether that integer is even or odd.

b = int (input ("Please enter a positive integer"))
d = 2
m = 3

# Loop will run until it reaches 1. **Don't put in >= 1 or it will create infinte loop.
while b > 1:
        # Any number is even if after dividing by two there is no
        # remainder left over.
    if b % 2 == 0:
            # If integer is even it will be divided by two until it
            # reaches an odd integer.
        b = b/d
        print(b)
        # If remainder is not equal to zero when divided by two then integer is odd.
    elif b % d != 0:
            # If integer is odd it will be multiplied by 3 and 1 added to this answer.
        b = (b*m)+1
        print(b)