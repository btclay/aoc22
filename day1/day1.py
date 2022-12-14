#!/usr/bin/env python3
import string
import numpy

filename = "input.txt"

total_snacks = []

with open(filename) as inputfile:
	datastream = inputfile.read()
	datastream = datastream.split("\n\n")

for elf_num, elf_snacks in enumerate(datastream):
	elf_snacks = elf_snacks.split()
	total = 0
	for snack in elf_snacks:
		if snack == "\n":
			break
		total = int(snack) + total
	total_snacks.append(total)

most_snacks = numpy.argmax(total_snacks)

print ("Elf with the most snacks is elf number", most_snacks)
print("They are carrying", total_snacks[most_snacks], "calories")


total_snacks.sort(reverse=True)

top3 = total_snacks[0] + total_snacks[1] + total_snacks[2]
print("Total carried by the top 3 elves is", top3)
