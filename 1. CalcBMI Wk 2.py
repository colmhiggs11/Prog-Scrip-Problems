# Colm Higgins 
# This program will calculate the of BMI for a certain individual 
# from the inputs of their weight(Kg) & Height(cm)

# User inputted weight in (Kg) and Height in (cm)
weight = float (input("Enter weight in Kg:\n"))
height = float (input("Enter height in cm's:\n"))

# Formula for calcuating BMI
BMI = weight / ((height/100)**2)

# Rounding BMI to decimal place found on Stackoverflow
# https://stackoverflow.com/questions/2075128/python-print-all-floats-to-2-decimal-places-in-output

print("Your BMI is ",format(BMI,'.2f'))