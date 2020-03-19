# Colm Higgins
# This program will display a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np 
import matplotlib.pyplot as plt

a = float(input("Enter the first point of the range\n"))
b = float(input("Enter the last point of the range \n"))
c = float(input("Enter the increments you want the range to incease in\n"))

x = np.arange(a,b,c)
f_x = x
g_x = f_x**2
h_x = f_x**3

print(f_x,g_x,h_x)
plt.plot(f_x,"gs", label = "x")
plt.plot(g_x,"r^", label = "x^2")
plt.plot(h_x,".b", label = "x^3")
plt.legend()
plt.title("Functions of x , x^2 & x^3")
plt.show()