#!/usr/bin/env python
import sys
# pip install openssh_wrapper
from openssh_wrapper import SSHConnection

def usage():
    print("""PySSH

USAGE : pyssh <host> <command(s)>
         pyssh <-i|--interactive> : Interactive mode 

""")

def run(host, cmd):
    print("Sending command " + (cmd) + "to host " + (host))
    conn = SSHConnection(host)
    ret = conn.run(cmd)
    print(ret)


try:
    args = sys.argv[0:1]
except IndexError:
    usage()
    sys.exit(1)

if not len(args) >= 2:
    for arg in args:
        host = sys.argv[1]
        cmd = sys.argv[2]
        try:
            run(host, cmd)
        except NameError:
            print("No command sent...")

elif len (args) <= 2:
    usage()

        
