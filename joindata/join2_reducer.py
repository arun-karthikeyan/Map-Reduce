#!/usr/bin/env python

import sys

isABCShow = False

show_total_views = 0

prev_show = " "

for line in sys.stdin:
	line = line.strip()
	curr_row = line.split('\t')
	curr_show = curr_row[0]

	if curr_show != prev_show:
		if isABCShow:
			print('{0}\t{1}'.format(prev_show, show_total_views))
		#Reset Everything		
		prev_show=curr_show
		isABCShow = False
		show_total_views = 0	

	if curr_row[1].isdigit():
		show_total_views = show_total_views + int(curr_row[1])
	else:
		isABCShow = True	#We know it has to be ABC Show because we've already filtered out the other ones in the mapper

if isABCShow:	#Handling the last row
	print('{0}\t{1}'.format(prev_show, show_total_views))
