#!/usr/bin/env python

import sys

#This mapper code will input a <date word, value> input file (fileA) or <word, value> input file (fileB), and move date into the value field for output

for line in sys.stdin:
	line = line.strip()
	key_value = line.split(",")
	key_in = key_value[0].split()
	value_in = key_value[1]

	#print key_in
	if len(key_in)>1:	#Then it means it contains fileA
		date = key_in[0]
		word = key_in[1]
		value_out = date+" "+value_in
		print('%s\t%s' % (word, value_out))
	else:
		print('%s\t%s' % (key_in[0], value_in))


#"\t" coz hadoop expects a tab to separate key value but this program assumes the input file has a ',' separating key value.
