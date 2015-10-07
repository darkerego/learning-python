#!/usr/bin/python
######################
# Two Integers
# DarkerEgo's Python Homework ;-/
# 9/15/15
#

print ("""
##                   ## Two Integers ##                ##
#########################################################
## Enter two whole numbers and they shall be examined  ##
## mathematically. Sum, Dif, Avg, Max, Min, Dist, Etc! ##
#########################################################
""")


while True:
    try:
        int1 = int(input("Enter a number: "))
        break
    except ValueError:
        print ("That was no valid number.  Try again...")


while True:
    try:
        int2 = float(input("Enter a number: "))
        break
    except ValueError:
        print ("That was no valid number.  Try again...")


# formulas to get sum, diff, prod, average, min, max

sum1 = int1 + int2 # called sum1 because sum is a constant function
diff = int1 - int2
product = int1 * int2
average = (sum1 / 2) 
maxINT = max(int1,int2)
minINT = min (int1, int2)
distance = abs(int1 - int2)

# this is just a way to display the results via for-loop. If sum is
# 2 than we're saying dispSUM = "Sum : 2" , or "text: $variable"

dispSUM =  "Sum: %s" % sum1
dispDIFF = "Difference: %s" % diff
dispPROD = "Product: %s" % product
dispAV = "Average: %s" % average
dispMAX = "Maxinum: %s" % maxINT
dispMIN = "Minimum: %s" % minINT
# 
dispABS = "Absolute Difference: %s" % distance
# for each thing, print it!

for i in (dispSUM, dispDIFF, dispPROD, dispAV, dispMAX, dispMIN, dispABS):
    print (i)

input("Press Enter To Quit...")
