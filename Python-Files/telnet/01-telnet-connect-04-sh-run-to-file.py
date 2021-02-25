#!/usr/bin/env python3

# this will telnet into a remote Cisco router and execute the command:
#  "show ip interface brief"
import getpass
import telnetlib
import os

HOST = "10.99.99.11"
user = input("Enter your remote username: ")
password = getpass.getpass()

# Opens the file for overwrite access
ouput_file = open(f'config-from-router-1.cfg', 'w')

# the following two lines could combine: telnet_connection_1 = telnetlib.Telnet(HOST)
telnet_connection_1 = telnetlib.Telnet()
telnet_connection_1.open(HOST)

telnet_connection_1.read_until(b"username: ",3)
telnet_connection_1.write(user.encode("ascii") + b"\n")
if password:
   telnet_connection_1.read_until(b"Password:",3)
   telnet_connection_1.write(password.encode("ascii") + b"\n")


# Prompt for enable password and then read in.
print("Enter your enable password: ")
# enable_password = getpass.getpass()
enable_password = 'cisco'

telnet_connection_1.write(b"enable\n")
telnet_connection_1.read_until(b"Password:",3)
telnet_connection_1.write(enable_password.encode("ascii") + b"\n")

# This makes it so that if a show gives lots of output
# it doesn't wait for a spacebar to be pressed to get the next page.
telnet_connection_1.write(b"terminal length 0\n")

telnet_connection_1.write(b"sh run\n")

# read a single line from the telnet session
nextline = telnet_connection_1.read_until(b"\n", 3)
while nextline :
    # write the line to file
    ouput_file.write(nextline.decode('ascii'))
    print (nextline.decode('UTF-8'))
    nextline = telnet_connection_1.read_until(b"\n", 3)

# disconnect the other end
telnet_connection_1.write(b"exit\n")

# close this end
telnet_connection_1.close()  
