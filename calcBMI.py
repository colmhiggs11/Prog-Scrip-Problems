# This will be a calculation of BMI for a certain individual

#For anyone that wants to input their own weight use below code and remove comments
#weight = float (input("Enter weight:"))
#height = float (input("Enter height:"))

#weight in kg
weight = 65
#height in cm
height = 180

BMI = weight / ((height/100)**2)
#Rounding BMI to decimal place

print(format(BMI,'.2f'))