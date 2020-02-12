## Part 1 - Lab week 3 
## Program to take input of name and print Hello "name"

# 1 name =  str(input("Enter you name :"))

# 1 print("Hello {} ".format(name))


## Part 2 
## Subtract 1st num from 2nd num and print

# 2 x = int(input("Please Enter first Number :",))
# 2 y = int(input("Please Enter second Number :"))
# 2 answer = x - y

# 2 print(" {} minus {} is {} ".format(x, y, answer))

## Part 3 
## Divide 1st num by second num, give result and remainder

# 3 x = int(input("Enter first number: "))
# 3 y = int(input("Enter second number: "))

# 3 div = int(x/y)
# 3 rem = x%y

# 3 print("{} divided by {} is {} with a remainder of {}".format(x, y, div, rem))

## Part 4
## Prints out a random number from 1 - 10

# 4 import random

# 4 a = int(input("Enter 1st value in range "))
# 4 b = int(input("Enter 2nd value in range "))

# 4 num = random.randint(a,b)
# 4 print("Your random number is {}".format(num))

## Part 5
## Normalising a string and printing original and new characters

# 5 rs = (input("Please enter original raw String "))

# 5 normrs = rs.strip().upper()

# 5 lenrs = len(rs)
# 5 lennormrs = len(normrs)

# 5 print("The string you entered shouting is : {}!!!!! ".format(normrs))
# 5 print("We have shortened the number of characters from {} to {} ".format(lenrs, lennormrs))

## Part 6 & 7
## Program to print out a random fruit  

# 6 import random

# 6 fruits = 'Apple', 'Orange', 'Pear','Banana', 'Kiwi'

# 6 ranfruit = random.randint(0,len(fruits)-1)

# 6 fruit = fruits[ranfruit]

# 6 print("Your random fruit is: {}".format(fruit))
# 6 print(fruits[-5])

## Part 8
## Dictionaries
## Creating a dictionary object 

currentboook = { 'Title' :"A Whirlwind Tour of Python",
 'Author' :"Colm Higgins",
  'Price' :100 }

#print(currentboook)
#print(currentboook["Author"])

currentboook["ISBN"] = 12534087

print("currentbook has these values: ")
for attri in currentboook.values():
    print("    => {}".format(attri))