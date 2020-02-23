# Colm Higgins
# Create a function to return squareroot of the input

### x1 = float (input("Enter the value you want to get the SQRT of "))

### x2 = x1**0.5

### print("The square root of {} is {}".format(x1,x2))

b = float(input("Enter the number you want to get Square root approximtaion using Newton Raphson method "))


def newton_approx(x,iter = 500):
    
    for b in range(iter): # iteration number
        x = 0.5 * (x + b / x) # update
        #x = (x - (x**2 - N) / (x*2)) # update
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return x


print(newton_approx(b))