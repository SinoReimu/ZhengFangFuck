#!/usr/bin/python
import os

list = open('list.txt')
while 1:
    line = list.readline()
    array = line.split()
    if len(array) < 2:
    	break
    number = array[0]
    password = array[1]
    if not line:
    	break
    os.system('./login.py '+number+' '+password)
    print number + ' checked'
