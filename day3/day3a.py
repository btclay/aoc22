#!/usr/bin/env python3
import string

filename = "input.txt"

alfa = string.ascii_lowercase + string.ascii_uppercase

priority = dict([(x[1],x[0]) for x in enumerate(alfa)])


with open(filename) as inputfile:
	datastream = inputfile.read()
	datastream = datastream.split()

rucksacks = []

sum = 0

for line in datastream:
	rucksacks.append([line[:len(line)//2], line[len(line)//2:]])

for sack in rucksacks:
	left_side = set(list(sack[0]))
	right_side = set(list(sack[1]))

	common = left_side.intersection(right_side)

	sum = sum + priority[list(common)[0]] + 1

print(sum)