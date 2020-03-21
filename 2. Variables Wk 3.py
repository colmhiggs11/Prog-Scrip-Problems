## Colm Higgins 
## This program will ask the user to input a string and prints
## every second letter in reverse order

# input sentence
x = input("Please type a sentence of your choice:  ")
# print input removing every 2nd letter and reversed 
# [::2] is every 2nd letter and putting a - before will reverse it.
# Shortening to [::-2] came from https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
print("The sentence you typed removing every second letter and reversed is:\n {}".format(x[::-2]))