#!/usr/bin/python
# H20 Boiling Point @ +/- Altitude
# Assignment If Choice
# September 26th, 2015
# Version ~ 20ish
########################
import re
import sys
t=""
a=""
alt=""
temp=""
def getALT():
    alt = str(input("Enter altitude above altlevel, format 100M/F :"))
    if not re.match(r'[0-9]*[fFmM]$', alt):
        raise ValueError('')
    else:
        return alt
    
while True:
        try:
            alt = getALT()
            break
        except ValueError:("")

def getTEMP():
    temp = str(input("Tempurature in format 70C/F :"))
    if not re.match(r'[0-9]*[fFcC]$', temp):
        raise ValueError('')
    else:
        return temp

while True:
    try:
        temp = getTEMP()
        break
    except ValueError:("")


a = ''.join(x for x in alt if x.isdigit())

t = ''.join(x for x in temp if x.isdigit())

t = float(t)
a = int(a)

#if "C" or "c" in temp:
def calcCEL():
    tI = (100 - a * 0.00552)
    tC = (100 - tI)
    tB = 100 - (tC)
    tF = 0 - (tC)
    print ('Altitude in M: %s' % (a))
    print ('Temp in C is: %s' % (t))
    print ('Temp change at alt is: %s' % (tC))
    print("Boiling point in C of H20 at altitude: %s" % (tB))
    print ('Freezing point at alt is: %s' % (tF))
    

    if t > (tF) and t < (tB):
        print("Liquid")

    elif tB <= (tF):
        print("Solid")
            
    elif t >= (tB):
        print("Gas")
        sys.exit(1)


#    else:
def calcFAR():
        tI = (212 - a * 0.00184)
        tC = (212 - (tI))
        tB = (212 - (tC))
        tF = 32 - (tC)

        print ('Altitude in F: %s' % (a))
        print ('Temp in F is: %s' % (t))
        print ('Temp change at alt is: %s' % (tC))
        print ('Boiling point at alt is: %s' % (tB))
        print ('Freezing point at alt is: %s' % (tF))
        if t > (tF) and t < (tB):
            print("Liquid")

        if t <= (tF):
            print("Solid")
            
        if t >= (tB):
            print("Gas")

if re.match(r'[0-9]*[mM]$', alt):
    calcCEL()
else:
    calcFAR()
