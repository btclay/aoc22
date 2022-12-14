#!/usr/bin/env python3
import string

filename = "input.txt"


with open(filename) as inputfile:
	datastream = inputfile.read()
	datastream = datastream.split()


elves = []

total_eclipse_of_the_tasks = 0

for item in datastream:
	elves.append(item.split(','))

for pair in elves:
	first_range = pair[0].split('-')
	second_range = pair[1].split('-')

	if int(first_range[0]) <= int(second_range[0]) and int(first_range[1]) >= int(second_range[1]):
		total_eclipse_of_the_tasks += 1

	elif int(second_range[0]) <= int(first_range[0]) and int(second_range[1]) >= int(first_range[1]):
		total_eclipse_of_the_tasks += 1

print(total_eclipse_of_the_tasks)
