# Colm Higgins
# Program to output whether or not today is a weekday or weekend.
# There are no date types in python but by importing the datetime module
# dates can be used as objects.
import datetime
# This will get the current date
datetime.datetime.now()
# Assigning that value to "now"
now = datetime.datetime.now()
# Assigning the value of the weekday to "tday"
tday = now.weekday()
# Values of weekend days are as follows [Saturday,Sunday] = [5,6]
# Values of weekdays are as follows [Monday,..,Friday] = [0,..,4]
if tday >= 5:
    tday = "weekend"
    # Will print if value for a >=5
    print("Thank God it's the",tday)  
elif tday <= 4:
    tday = "weekday"
    # Will print if a <= 4 and will also print "a" underlined
    # https://stackoverflow.com/questions/35401019/how-do-i-print-something-underlined-in-python
    print("Unfortunately today is tday","\u0332".join(tday))
        
            
