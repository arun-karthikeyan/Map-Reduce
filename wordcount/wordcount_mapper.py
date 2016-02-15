#!/usr/bin/env python
#the above just indicates to use python to interpret this file

#This mapper code will input a line of text and output <word, 1>

import sys	#a python module with system functions for this OS

# this 'for loop' will set 'line' to an input line from system standard input file

for line in sys.stdin:
	line = line.strip() #strip is a method used to stip off carriage return

	keys = line.split() #split line at blanks (by default)

	for key in keys:
		print('{0}\t1'.format(key))

#note that the hadoop default is 'tab' separates
