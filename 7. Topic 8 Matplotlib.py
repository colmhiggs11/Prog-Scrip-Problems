# Colm Higgins
# This program will display a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# Numpy package is imported to allow an array to be created
# using "arange" which returns evenly spaced values within a given interval. 
import numpy as np 
# Matplotlib is a plotting library in Python and pyplot is a collection of 
# functions in Matplotlib that can manipulate elements in plots
import matplotlib.pyplot as plt

# "a" asks for the first number in the range in the example below "0" which is 
# where the range will begin
# "b" asks for the second number in the range in the example below "15" which is
# where the range will end
# "c" asks for the third number in the range in the example below "1" which is 
# the step size. (this example would be every full integer)
# Eg.(0:15:1)
a = float(input("Enter the first point of the range\n"))
b = float(input("Enter the last point of the range \n"))
c = float(input("Enter the increments you want the range to incease in\n"))

# Arange returns evenly spaced values within a given interval. 
# The step size is specified.
x = np.arange(a,b,c)
# Assigning values to function variables.
f_x = x
g_x = f_x**2
h_x = f_x**3

print(f_x,g_x,h_x)
# Some extra formatting was found @ https://www.python-course.eu/matplotlib_subplots.php
# Plots the f_x function as green squares with the label "x"
plt.plot(f_x,"gs", label = "x")
# Plots the g_x function as red triangles with the label "x^2"
plt.plot(g_x,"r^", label = "x^2")
# Plots the h_x function as blue dots with the label "x^3"
plt.plot(h_x,".b", label = "x^3")
# Puts the legend on the plot.
plt.legend()
# Gives a title to the legend.
plt.title("Functions of x , x^2 & x^3")
# Makes the plot appear as a pop up.
plt.show()