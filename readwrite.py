#!/usr/bin/env python
#

# Open a file and read it line by line, number the lines
#(/* 1 */ line1)
#/* 2 */ line2)
# need sys
import sys
#inF = ""
#outF = ""
# initialize line #
lineNumber = 0
# cli args
"""
try:
    opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
except getopt.GetoptError, err: 
    usage(err)

for opt, arg in opts:
    if opt in ('-h', '--help'): 
        usage()

if len(args) != 1:
    usage("specify thing...")
"""

import sys

try:
    args = sys.argv[0:2]
except IndexError:
    print("Usage: script input output (files)")
    sys.exit(1)
# ask for input if no arguments given
if len(args) >= 1:
    inF = str(input("File to open: "))
    outF = str(input("File to save into: "))
# otherwise use args as files
else:
    #script, inF, outF = args
    for arg in args:
        inF = sys.argv[1]
        outF = sys.argv[2]
# open files
open(sys.argv[1], 'r')
        
open(sys.argv[2], 'w+')
# define read/write
read = open(inF, "r")
write = open(outF, "w")
# Shift +1 each line
lineNumber += 1
# format each line and write it
for line in read:
    write.write("/* %s */ %s" % (lineNumber, line))
    lineNumber += 1

#close files    
read.close()
write.close()
    
