# Colm Higgins
# This program will approximate the squareroot of the input using Newton Raphsons Method
# for Approximating Square Roots.

def new_raph(N):
    x0 = N/2
    fxn = (x0**2) - N
    while fxn>0.1:
        fxn = (x0**2) - N
        fpxn = (2*x0)
        x1 = x0 - (fxn) / (fpxn)
        if fxn <= 0.1:
            print('Final Approximation of the Sqrt to 2 decimal places is:\n',format(x1,'.2f'))
        else:
            x0 = x1
            print(format(x1,'.2f'))
   
new_raph(float(input("Enter positive number you are looking for approximate sqrt for  ")))

