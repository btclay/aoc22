#!/usr/bin/env python3
import string

filename = "input.txt"

score = 0

opp_rock = "A"
opp_paper = "B"
opp_scissors = "C"

p_rock = "X"
p_paper = "Y"
p_scissors = "Z"

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

guide = []

with open(filename) as inputfile:
	datastream = inputfile.read()
	datastream = datastream.split('\n')

for item in datastream:
	item = item.split()
	guide.append(item)

guide.pop() #remove blank entry at end


def rpsResult(opponent, player):
	points = 0
	match opponent:
		case "A":
			match player:
				case "X":
					points = draw + rock
				case "Y":
					points = win + paper
				case "Z":
					points = lose + scissors
		case "B":
			match player:
				case "X":
					points = lose + rock
				case "Y":
					points = draw + paper
				case "Z":
					points = win + scissors
		case "C":
			match player:
				case "X":
					points = win + rock
				case "Y":
					points = lose + paper
				case "Z":
					points = draw + scissors

	return points

for round in guide:
	score = score + rpsResult(round[0], round[1])

print("Score is", score)

