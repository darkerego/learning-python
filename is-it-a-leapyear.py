#!/usr/bin/python env
# Leap Year Calculator
# Darkego's Python Homework ;/
# year divisible by 4 and 400 and not divisible by 100
import sys
year = ""
print("""
####################
# Is it leap year? #
####################

""")
# See comments below
import calendar

# Just another of saying true

while 1 == 1:
    try:
        
        y = int(input("Please enter a year...: "))
        break
    except ValueError:("That's not a year!")
    

#############################################
# Book's logic:
#
#if (y%4 or y%400) and not (y%100):
#    print("%s is a leap year!" % y)
#else:
#    print ("%s is not a leap year!" % y)
##############################################
#
# This would do it but its not a single if statement:
#def isLEAP():
#    if y % 400 == 0:
#        Return True
#    if y % 100 == 0:
#       Return False
#    if y % 4 == 0:
#        Return True
#    else:
#        Return False

# This does do it but its better to trust the library that's already meticoulousy written...


def isLEAP(year):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

# 
#if isLEAP(year):
#    print ("Math says %s a leapyear!" % y)
#elif not isLEAP(year):
#    print("Math says not...")

# But I can still pull it off using the math and the library in one if statement, for the
# sake of ultimate reliability.

if calendar.isleap(y) and isLEAP(year):
    print ("Python and our math says %s is a leap year!" % y)
else:
    print ("Python and our math says %s is not a leap year!" % y)

# Probably a good habbit to make sure your programs are closing, right?
sys.exit(0)
