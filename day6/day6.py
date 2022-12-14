#!/usr/bin/env python3
import string
import collections

filename = "input.txt"

with open(filename) as inputfile:
	datastream = inputfile.read()
	datastream = list(datastream)

last4 = collections.deque(maxlen=4) #create a deque with maxlen 4 so we can continually push the next char in as we read them
last14 = collections.deque(maxlen=14)

packet_start_found = False
message_start_found = False

for index, element in enumerate(datastream): 
	last4.append(element)
	last14.append(element)

	if packet_start_found and message_start_found:
		break

	if len(set(last4)) == 4 and not packet_start_found: #check if the contents of the deque are four unique values
		print("Packet start at", index + 1) # Plus one since we want the next character
		packet_start_found = True
	
	if len(set(last14)) == 14 and not message_start_found: #same as before, but 14 since we are looking for start of message marker
		print("Message start at", index + 1)
		message_start_found = True
