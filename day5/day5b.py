#!/usr/bin/env python3

#    [W]         [J]     [J]        
#    [V]     [F] [F] [S] [S]        
#    [S] [M] [R] [W] [M] [C]        
#    [M] [G] [W] [S] [F] [G]     [C]
#[W] [P] [S] [M] [H] [N] [F]     [L]
#[R] [H] [T] [D] [L] [D] [D] [B] [W]
#[T] [C] [L] [H] [Q] [J] [B] [T] [N]
#[G] [G] [C] [J] [P] [P] [Z] [R] [H]
# 1   2   3   4   5   6   7   8   9 

import string
from dataclasses import dataclass

stacks = [[]]*10
stacks[1] = ['G','T','R','W']
stacks[2] = ['G','C','H','P','M','S','V','W']
stacks[3] = ['C','L','T','S','G','M']
stacks[4] = ['J','H','D','M','W','R','F']
stacks[5] = ['P','Q','L','H','S','W','F','J']
stacks[6] = ['P','J','D','N','F','M','S']
stacks[7] = ['Z','B','D','F','G','C','S','J']
stacks[8] = ['R','T','B']
stacks[9] = ['H','N','W','L','C']


#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 

#stacks = [[]]*4
#stacks[1] = ['Z','N']
#stacks[2] = ['M','C','D']
#stacks[3] = ['P']



filename = "input.txt"

@dataclass
class Instruction:
    count: int 
    src: int 
    dst: int

operations = []

with open(filename) as inputfile:
	for line in inputfile:
		if 'move' in line:
			read_line = line.split()
			operations.append(Instruction(int(read_line[1]),int(read_line[3]), int(read_line[5])))


for i, step in enumerate(operations):
	#for i in range(step.count):
	#	stacks[step.dst].append(stacks[step.src].pop())
	stacks[step.dst].extend(stacks[step.src][-step.count:])
	for i in range(step.count):
		stacks[step.src].pop()



for i, stack in enumerate(stacks):
	if i: print("Stack", i, "top value is", stack[-1])
