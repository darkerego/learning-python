#!/usr/bin/python
# Standard 15% Tip Calculator
# Author Darkerego
# Written September 10th, 2015
############################
# PSEUDOCODE:
#############################
#input (tip percentage)
#while true: try (value error, break, input again)
#input subtotal of meal
#while true: try input(total)
#calculate (subtotal * tip / 100 + subtotal)
#input(num ppl splitting cost)
#while true: try (input), (break) read input again)
# cost per person = total / people splitting total
#
#eachCOST = (subTTL * intTIP / 100 + subTTL / splitCOST)

print ("\n")
#

while True:
    try:
        tip = int(input("Enter tip in Percentage (ex. 15): %"))
        break
    except ValueError:
        print ("That was no valid number.  Try again...")   # check input. if there is an error,
                                                            # show error message and try again.
while True:
    try:
        subTTL = float(input("Enter subtotal of meal): $"))
        break
    except ValueError:
        print ("That was not a valid decimal number.  Try again...")


TTL = (tip * subTTL / 100 + subTTL )           # algerithm for calculating TTL. (%tip * subtotal / 100 + subtotal)
fltTTL = float(TTL)     # declare fltTTL as datatype float


while True:
    try:
        splitCOST = int(input("Enter number of people splitting bill (ex. 3): "))
        break
    except ValueError:
        print ("That was not a valid number.  Try again...")

eachCOST = fltTTL / splitCOST    # Calculate cost of each person by dividing fltTTL by intCOST

print ("--------------------------")
print ("#   ----- TOTALS:-----   #")
print ("--------------------------")
print ("Tip Percentage: %", (tip))
print ("Subtotal before tip: $", subTTL)
print ("Grand total cost w/ tip: $", round (fltTTL,2))  # Print fltTTL but round it to 2 decimals because
                                                                # we're dealing with currency

print ("Cost per individual: $", round (eachCOST,2))    # Print cost per person to stout (stored as eachCOST and rounded to
                                                    # 2 decimals again.


