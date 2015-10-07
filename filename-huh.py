#!/usr/bin/python
# DarerEgo's Python Homework [Sept 17, '15]
# URI PATH ... Formation?
##########################
import re

def get_FILE():
    file = input("What is the name of the file? :")

    if not re.match(r'^[a-z-A-Z-0-9]*$', file):
                raise ValueError('')
    else:
        return file

def get_EXT():
    ext = input("What is the file extension? (Enter with the dot '.') :")
    if not re.match(r'[.[a-z-A-Z-0-9]*$', ext):
                    raise ValueError('')
    else:
        return ext
def get_URI():

    path = input ("Where is the file located (No trailing slash please) :")
    if not re.match (r'[\/[a-z-A-Z-0-9]*]*$', path):
                    raise ValueError('')
    else:
        return path

while True:
    try:
        file = get_FILE()
        break
    except ValueError:('')

while True:
    try:
        ext = get_EXT()
        break
    except ValueError:('')

while True:
    try:
        path = get_URI()
        break
    except ValueError:('')


print ((path)+"/"+(file)+(ext))

input("Press Enter to Quit...")
