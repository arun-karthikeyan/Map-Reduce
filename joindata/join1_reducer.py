#!/usr/bin/env python
import sys

#This reducer code will input a <word, value> input file, and join words together
#Note that the input will come as a group of lines with same word

#The program keeps track of current word and previous word, if word changes then it will perform the 'join' on the set of held values by merely printing out the word and values.

#In other words, no need to match keys explicitly, hadoop logistics has already shuffled and grouped them

prev_word = " "
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

dates_to_output = []
day_cnts_to_output = []

line_cnt = 0

for line in sys.stdin:
	line = line.strip()
	key_value = line.split('\t')
	line_cnt = line_cnt + 1
	curr_word = key_value[0]
	curr_value = key_value[1]

	if curr_word != prev_word:
		if line_cnt>1:		
			for i in range(len(dates_to_output)):
				v1 = dates_to_output[i]
				v2 = day_cnts_to_output[i]				
				print('{0} {1} {2} {3}'.format(dates_to_output[i], prev_word, day_cnts_to_output[i], curr_word_total_cnt))
			#resetting the lists after printing
			dates_to_output = []
			day_cnts_to_output = []
		prev_word = curr_word
	
	if(curr_value[0:3] in months):
		date_day = curr_value.split()
		dates_to_output.append(date_day[0])
		day_cnts_to_output.append(date_day[1])
	else:
		curr_word_total_cnt = curr_value		

#For the last index
for i in range(len(dates_to_output)):
	print('{0} {1} {2} {3}'.format(dates_to_output[i], prev_word, day_cnts_to_output[i], curr_word_total_cnt))
