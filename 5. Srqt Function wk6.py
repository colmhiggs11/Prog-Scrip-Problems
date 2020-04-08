# Colm Higgins
# This program will approximate the squareroot of the user input using Newton Raphsons Method
# for Approximating Square Roots.

# defining the function with the def statment. The parameter is listed as N.
# https://www.tutorialspoint.com/python3/python_tutorial.pdf
def new_raph(N):
    # variables assigned values
    x0 = N/2
    fxn = (x0**2) - N
    # while loop that gives parameters for code to run. If fxn = 0 then this is the actual sqrt.
    while fxn > 0.1:
        fxn = (x0**2) - N
        fpxn = (2*x0)
        # Newton Raphson method for Sqrt approximation
        x1 = x0 - (fxn) / (fpxn)
        # If/else loop to provide approximation
        if fxn <= 0.1:
            print('Final Approximation of the Sqrt to 2 decimal places is:\n',format(x1,'.2f'))
        else:
            # Value of x1 will be assigned to x0 and calculations will be updated.
            x0 = x1
            print(format(x1,'.2f'))

# Calling the function.
new_raph(float(input("Enter positive number you are looking for approximate sqrt for: \n")))

