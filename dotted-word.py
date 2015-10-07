#!/usr/bin/env python
# Darkerego's Python Homework ;-/
# Sep 25, 2015
# String Format V. 4:
# Print the first 3 letters, last three letters, \
# and whatever is in in the middle in dots (...):
# Mis...ipi


def print_dotted_word():
    word = str(input("What's the (7 letter or longer) word ?"))
    if len(word)<7:
        raise ValueError("Needs to be 7 letters.")
    print(word[:3] + '.'*(len(word)-6) + word[-3:])
    
while True:
    try:
        print_dotted_word()
        break
    except ValueError:("Needs to be 7 letters.")
