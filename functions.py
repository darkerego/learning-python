#/usr/bin/python env
# Nov 3, 2015
# Repeat, Flip, Count
#####################
# libs we need
import random,sys
#####################
# Error Messages
#####################
erNotInt = "Only integers make sense in this scenario."
erNoDelim = "I asked for a delimiter... it can be anything but a return..."
erDoesntWork = "I can't effectively scramble words less than 4 letters. How did you even get this far?"
########################
# repetition,repetition, -,
########################


# I love one liners
def repeat(string, n, delim):
    new_string = ((((string) + (delim)) * n)[:-1])
    return new_string

####################
# Count the vowels 
####################
def countVowels(s):
    
    num_v = 0
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    x = len(s);y = range(x)
    # I borrowed most of this from a previous  assignment. Seems backwards.. \
    # i.e. 'for 'string' in 'vowels' .. \
    # humans would think 'for vowels in strings'
    for i in y:
        if s[i] in vowels:
            num_v += 1
    return (num_v)
            

#######################
# Selbmarcd Snirtg    #
#######################


def scramble(sc):
    scrambled = sc[0]
    # reverse whats inbetween first and last chars
    if len(sc) >= 4:
        for i in range(len(sc) - 2, 0, -1):
            scrambled += sc[i]
        scrambled += sc[len(sc) - 1]
    else:
        scrambled = (erDoesntWork)
    return scrambled

#########################
# Check and Exec!       #
#########################
def execute():
    print("""
,-.                      .   .   ,--. .       .    ,-.             .   . 
|  )                     |   |   |    | o     |   /                |   | 
|-<  ,-. ,-: ;-. ,-. ,-: |-  |   |-   | . ;-. |   |    ,-. . . ;-. |-  | 
|  \ |-' | | | | |-' | | |       |    | | | |     \    | | | | | | |     
'  ' `-' `-` |-' `-' `-` `-' o   '    ' ' |-' o    `-' `-' `-` ' ' `-' o 
             '                            '                              
    """)
    # String should be at least 4 chars for these funcs to make sense
    while 1:
        string=str(input("Give me a string... : "))
        if string and len(string) >= 4 or not string.isspace:
            break
        else:
            continue
    # assigning equal variables for use in different functions, \
    # as not to confuse Python.
    s = string
    sc = string

    # Make sure we've got an integer
    while 1:
        try:
            n = int(input("How many times shall I repeat it? Enter an integer :"))
            break
        except ValueError:
            print(erNotInt)
    
    while 1:
        # ... and a delimiter
        delim = str(input("Enter a delimiter :"))
        if len(delim) >= 1 and delim:
            break
        else:
            print(erNoDelim)
            continue
    # The fun stuff. Printing the input, fed to each function and returned.
    print("Your repeated, delimited string: ")
    print(repeat(string, n, delim))
    print("Number of vowels in %s :" % s)
    print(countVowels(s))
    print("%s scrambled :" % sc)
    print(scramble(sc))
# run
execute()
# exit cleanly
sys.exit(0)
