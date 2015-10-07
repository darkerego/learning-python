#!/usr/bin/env python
#####################
# note to self: [python env] \
# makes no sense, python \
# takes no such argument
######################
# Auth DarkerEgo
# Written Oct 6, 2015
# Integer To Roman
# Version 3:
# Added re-exec & comments)
######################
# Error Messages
erNoValidInt = ("Valid integers less than 4000 only!")
# Assign Variables
integer = ""
# Program Description
print("""

,-.-. .-.______2,---.   .---.          .--. .-. .-. 
|(|  \| |__   __| .-.\ / .-. )|\    /|/ /\ \|  \| | 
(_|   | | )| |  | `-'/ | | |(_|(\  / / /__\ |   | | 
| | |\  |(_) |  |   (  | | | |(_)\/  |  __  | |\  | 
| | | |)|  | |  | |\ \ \ `-' /| \  / | |  |)| | |)| 
`-/(  (_)  `-'  |_| \)\ )---' | |\/| |_|  (_/(  (_) 
 (__)               (__(_)    '-'  '-'     (__)     

     Converts your integer (=<4999) to Roman Numerals!

""")

# Define function to get integer to convert
# Ensure <= 3999

def get_INT():
    while True:
        try:
            integer = int(input("Enter a number: "))
            if (integer) <= 3999:
                return integer
                break
        except ValueError:("")
        print (erNoValidInt)

           
# Improved exit function. Exit or run again

def exit_0():
    while True:
        try:
            x = input('\nPress "Ctrl" + "C" to quit or "Enter" to Convert Another :')
            if (x) == "":
                execute()
        except KeyboardInterrupt:
                break
                exit(0)
# Legend for conversion. [Another case of "why reinvent the wheel?": \
# {import roman; r = roman.toRoman(n)} would suffice ;)]

def conv_ROMAN (integer):
    results=''
    legend=(('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),
            ('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1))
    parts = []
    for letter, value in legend:
        while value <= integer:
            integer -= value
            parts.append(letter)
    return ''.join(parts)

# If our program is contained within a function, \
# we can loop it for easy re-execution

def execute():
    integer = get_INT()
    results = conv_ROMAN(integer)
    print("#########################\n# Roman Numeral Format: # \n#########################")
    print("     %s    " % (results))

# Piecing it together:
# get int; get value of letters for ints in legend; join only letters; \
# print results; exit w/ status 0!


execute()
exit_0()
