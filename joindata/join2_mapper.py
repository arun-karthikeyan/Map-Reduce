#!/usr/bin/env python

import sys

#The mapper helps get rid of TV shows that are not showcasted in ABC Channel

abc = 'ABC'

for line in sys.stdin:
	line = line.strip() #Get's rid of extra chars at the end
	current_row = line.split(",")
	show = current_row[0]
	
	if current_row[1].isdigit():
		#Now we know that the file belongs to join2_gennum*, so just print it
		print('{0}\t{1}'.format(show, current_row[1]))
	else:
		if abc == current_row[1]:
			print('{0}\t{1}'.format(show, current_row[1]))
