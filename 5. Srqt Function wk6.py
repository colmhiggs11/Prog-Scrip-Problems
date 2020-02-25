# Colm Higgins
# Create a function to return squareroot of the input

### x1 = float (input("Enter the value you want to get the SQRT of "))

### x2 = x1**0.5

### print("The square root of {} is {}".format(x1,x2))
#b = float(input("Enter the number you want to get Square root approximtaion using Newton Raphson method "))
#def newton_approx(x, ):
   
   # b = 9
    #for b in range(1,iter): # iteration number
   # x = b//2
   # x = 0.5 * (x + b / x) # update
        #x = (x - (x**2 - N) / (x*2)) # update
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
 #   return x
#print(newton_approx(x))

#newton_approx(x)
#x = int(input("Enter first num"))
#y = int(input("Enter second num"))

#def smaller_num(x,y):
#x = int(input("Enter first num"))
#y = int(input("Enter second num"))
 #   if x>y:
  #      number = y
   # else:
    #    number = x
    #return number

#print("Smaller num is " ,(smaller_num(x,y)))

#small = smaller_num(y)

N = int(input("Enter number you are looking for approximate sqrt  "))
x = N/2
def f(x,N):
    fxn = x**2 - N  

    if fxn == 0:
        print(x)
    elif fxn !=0:
        fxn = x
        fxn = x**2 - N
        fpxn = 2*x
        sqrt = x - (fxn) / (fpxn)
        if fxn == 0:
            print(sqrt)
        else:
            fxn = sqrt            
            fxn = x**2 - N
            fpxn = 2*x
            sqrt = x - (fxn) / (fpxn)
            print(sqrt)
                

f(x, N)

