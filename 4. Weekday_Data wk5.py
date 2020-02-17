# Colm Higgins
# Program to output whether or not today is a weekday.

import datetime
datetime.datetime.now()

now = datetime.datetime.now()

a = now.weekday()
   
while a < 6 > 0:
    if a > 4:
        a = "weekend"
        print("Thank God it's the",a)  
        break
    elif a < 5 >= 0:
        a = "weekday"
        print("Unfortunately its a",a)
        break
        

