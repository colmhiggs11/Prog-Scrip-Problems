# Colm Higgins
# Program to output whether or not today is a weekday or weekend.

import datetime
datetime.datetime.now()

now = datetime.datetime.now()

a = now.weekday()
# Values of weekend days are as follows [Saturday,Sunday] = [5,6]
# Values of weekdays are as follows [Monday,..,Friday] = [0,..,4]
if a >= 5:
    a = "weekend"
    # Will print if value for a >=5
    print("Thank God it's the",a)  
elif a <= 4:
    a = "weekday"
    # Will print if a <= 4 and will also print "a" underlined
    # https://stackoverflow.com/questions/35401019/how-do-i-print-something-underlined-in-python
    print("Unfortunately today is a","\u0332".join(a))
        
            
