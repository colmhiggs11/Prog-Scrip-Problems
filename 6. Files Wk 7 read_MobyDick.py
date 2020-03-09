# Colm Higgins
# This program will read in a .txt file and count 
# the number of chosen characters in that file.

# Inputs take in the required filepath & character to search
x = input("Enter directory of file\n")
y = input("\nWhat character do you want to find the number of?\n")

# Opens & reads the file as f. Prints outputs
with open(x,'r') as f:
    print("The letter {} is used".format(y),f.read().count(y),"times")