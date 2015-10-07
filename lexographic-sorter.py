#!/usr/bin/python3.4 env
# -*- coding: utf-8 -*-
#####################################
# Algerithm (for doing this manually)
#
# if: (a > b > c):
#    print(a, b, c)
# elif (a > c > b):
#   print(a, c, b)
# elif (b > a < c):
#   print(b, c, a)
# elif (b > a > c):
#   print(b, a, c)
# elif (c > b < a):
#    print(c, b, a)
# elif (c > b < a):
#   print(c, a, b)
#
####################################

print("""

╦  ┌─┐═╗ ╦┬╔═╗┌─┐╔═╗┬─┐╔═╗┌─┐╦ ╦┬╔═╗  ┌─┐╔═╗┬─┐╔╦╗┌─┐╦═╗
║  ├┤ ╔╩╦╝│║  │ │║ ╦├┬┘╠═╣├─┘╠═╣│║    └─┐║ ║├┬┘ ║ ├┤ ╠╦╝
╩═╝└─┘╩ ╚═┴╚═╝└─┘╚═╝┴└─╩ ╩┴  ╩ ╩┴╚═╝  └─┘╚═╝┴└─ ╩ └─┘╩╚═
--------------------------------------------------------
    - Sorts Strings in Lexicographical Order -
       -------------------------------------         
""")
#
#
# Assignment P3.16
# Darkerego's Python Homework :-/
# Oct 1 15
#
# It just irritates me to death that
# / older versions eval (input)
# / finally found a workaround

import sys

req_version = (3,3)
cur_version = sys.version_info

if not cur_version >= req_version:
    print ("Your Python interpreter is too old. Please consider upgrading.")
    exit(2)





# 
# Errors:
erNoComp = ("Sorry... that doesn't compute!")
erMathBroken = ("Math is *broken*! BAILING!")
# Outputs:
equal = """
    #########################
    # All strings are equal #
    #########################
"""

equalUp = """
    ###########################
    # All strings are equal   #
    #  when case is upper     #
    ###########################
"""

equalLo = """
    #########################
    # All strings are equal #
    # when case is lower    #
    #########################
"""
notEq = """
    ############################
    # All strings NOT equal    #
    #     in any case."        #
    ############################
"""

# exit cleanly:
def exit_0():
    while True:
        try:
            x = input('\nPress "Ctrl" + "C" to quit ')
        except KeyboardInterrupt:
                break
                exit(0)
                
#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@
## A better way to catch empty input:
# (till The End of Time); 
#
while 1:
#try; input(s1);
#
    try:
        s1 = str(input("Enter a string : "))
#
#if s1 != something;
#
        if not s1:
#
#raise ValueError; 
#
            raise ValueError('Cannot be empty')
        else:
#
#else get on with it!
#
            break
    except ValueError as e:
        print(e)
#
#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@

while not 0:
    try:
        s2 = str(input("Enter another string : "))
        if not s2:
            raise ValueError('Cannot be empty')
        else:
            break
    except ValueError as e:
        print(e)

while True:
    try:
        s3 = str(input("Enter yet another string : "))
        if not s3:
            raise ValueError('Cannot be empty')
        else:
            break
    except ValueError as e:
        print(e)

#@#@#@#@#@#@#@#@#@#@#@#@
## Equality for (ALL aLl all)!
#
if (s1 == s2 == s3):
    print(equal)
elif (s1.upper() == s2.upper() == s3.upper()):
    print(equalUp)
elif (s1.lower() == s2.lower() == s3.lower()):
    print(equalLo)
# otherwise, they're not *all* equal to eachother
elif ((s1 != s2 != s3) or (s1 != s2) or (s1 != s3) or (s2 != s3)):
    print(notEq)
# in case my math doesn't check out or math as a science breaks altogether...
# \ do not pass go or collect $200, exit with error status (1)
else:
    print(erMathBroken)
    exit(1)

# With programming, cutting corners implies cleverness,
# not laziness. Python is capable of figuring this out.

strings = [(s1), (s2), (s3)]
strings = sorted(strings)



print ("""
-------------------------
Lexographically Sorted :
-------------------------
""")

for x in (strings):
    
    print(x)
    
# Catch those pesky traceback errors when script completes

exit_0()
