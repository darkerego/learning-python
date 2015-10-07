#/usr/bin/env python
# Gasoline Efficency Evaluator
#
# Ask tank capacity, gas milage, and current cost of gas,
# returns cost per 100 miles travelled and fuel range.
#
# DarkerEgo's Python Homework
# Sep 29 2015
erNocompute = ("Sorry.. that does not compute.")
erNegative =  ("Sorry.. negative input doesn't make sense.")

while True:
    try:
        capacity = float(input("Enter Tank Capacity in no. Gallons: "))

    except ValueError:
        print (erNocompute)
        continue

    if capacity < 0:
        print (erNegative)
        continue
    else:
        break

while True:
    try:
        mpg = float(input("Whatcha get for MPG? :" ))
        
    except ValueError:
        print(erNocompute)
        continue

    if mpg < 0:
        print(erNegative)
        continue
    else:
        break

while True:
    try:
        gascost = float(input("How much is gas? :" ))
    except ValueError:
        print(erNocompute)
        continue

    if mpg < 0:
        print(erNegative)
        continue
    else:
        break

per100 = (gascost)*(100 / (mpg))
fuRange = ((mpg)*(capacity))

# Just for fun, if there's 5 or more decimals in
# per100 add 'uselessly precise' to the output

if (per100).is_integer():
    print("#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#")
    print("Than it costs you $ %s to drive 100 miles" % (per100))
elif '{0:.5f}'.format(per100):
    print("Than it costs you a (uselessly precise) $ %s to drive 100 miles" % (per100))



print("Your fuel range is %s miles." % fuRange)

input("Press Enter or Ctrl+C to Quit...")
