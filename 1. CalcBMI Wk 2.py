# Colm Higgins 
# This will be a calculation of BMI for a certain individual

#For anyone that wants to input their own weight use below code and remove comments
#weight = float (input("Enter weight:"))
#height = float (input("Enter height:"))

#weight in kg
weight = 65
#height in cm
height = 180

BMI = weight / ((height/100)**2)
#Rounding BMI to decimal place found on Stackoverflow
#https://stackoverflow.com/questions/2075128/python-print-all-floats-to-2-decimal-places-in-output

print(format(BMI,'.2f'))