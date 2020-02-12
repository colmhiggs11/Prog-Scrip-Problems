## Colm Higgins 
##Week 3 Programming homework

## Write a program that asks the user to input a string and prints
## every second letter in reverse order

#   input sentence
x = input("Please type a sentence of your choice:  ")
#   print input removing every 2nd letter and reversed
print("The sentence you typed removing every second letter and reversed is: {}".format(x[::-1][::2]))