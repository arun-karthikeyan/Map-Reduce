#!/usr/bin/env python

#This reducer code will input a line of text and output <word, total-count>

import sys

last_key = None #Initialize these variables
running_total = 0

for input_line in sys.stdin:
	input_line = input_line.strip()
	this_key, value = input_line.split("\t", 1) #The hadoop default is tab separated key value

	value = int(value) #int() will convert a string to integer
	
	if last_key == this_key:
		running_total += value
	else:
		if last_key:
			print( "{0}\t{1}".format(last_key, running_total))
		
		running_total = value
		last_key = this_key

if last_key==this_key:
	print("{0}\t{1}".format(last_key, running_total))
