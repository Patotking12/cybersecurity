#!/usr/bin/python3
import os #imports the os library to run shell commands with open(‘ip-list.txt’, ‘r’) as r: #opens the IP text files and reads it

for line in r: #strips whitespace
    line = line.rstrip() #iterates through the text file line by line
    command = str("nc -nc -w 1 -z" + line + "80")
    os.system(command) #runs the net at port scanner
r.close() #closes the text file