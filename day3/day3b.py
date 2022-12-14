#!/usr/bin/env python3
import string

filename = "input.txt"

alfa = string.ascii_lowercase + string.ascii_uppercase

priority = dict([(x[1],x[0]) for x in enumerate(alfa)])


with open(filename) as inputfile:
	datastream = inputfile.read()
	datastream = datastream.split()

rucksacks = datastream

sum = 0

group = [0, 0, 0]

for sack_index, sack_contents in enumerate(rucksacks):

	group[sack_index % 3] = sack_contents

	if sack_index % 3 == 2:
		common = set(list(group[0])).intersection(set(list(group[1]))).intersection(set(list(group[2])))
		
		sum = sum + priority[list(common)[0]] + 1

print(sum)
