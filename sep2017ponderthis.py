# Build the list of whatevers.
# from itertools import permutations
# pieces = "KQRrBbNN"
# starts = {''.join(p).upper() for p in permutations(pieces)
# 					 if p.index('B') % 2 != p.index('b') % 2 		# Bishop constraint
# 					 and ( p.index('r') < p.index('K') < p.index('R')	# King constraint
# 						   or p.index('R') < p.index('K') < p.index('r') ) }
#
#
# outstream = open("chess3.txt", "wb")
# for thing in starts:
# 	outstream.write("%s\n" % thing)
#
# outstream.close()

print "This is an edit to this file on the testing-new-files branch"

instream = open("chess3.txt", "rb")
starts = set(["%s" % line.strip() for line in instream])
# starts = set(["RNBQKBNR"])

# Declare variables.
currstart = ""
maincounter = 0
othercounter = 0

def foo(bar):
# Silly function for finding the mirror index of a given index between 2 and 5.
	if bar == 2:
		return 5
	elif bar == 3:
		return 4
	elif bar == 4:
		return 3
	elif bar == 5:
		return 2

# Helper function for figuring out if there is a bishop on the opposite half of the board from the queen that is on the same color square as the king.
def bishopvalid(currstart):
	kingdex = currstart.find("K")
	if currstart.find("Q") > 3:
		# check if bishop is in the first half of the string
		for i in range(1, 4):
			if currstart[i] == "B" and i % 2 != kingdex % 2:
				return true
		return False
	else:
		# check if bishop is in the second half of the string
		for i in range(4, 7):
			if currstart[i] == "B" and i % 2 != kingdex % 2:
				return true
		return False

def isattackingvalid(currstart):
	pass
# Noahnotes:
# 28 both unprotected cases, also still need to check for B/Q in corner edge cases with double pawn pussh being valid in
# if the queen or bishop is on B or G and the king is on E or D

# Loop through all the stuff
while (starts):
	currstart = starts.pop()
	kingdex = currstart.find("K")
	# Special case to deal with castling.
	if (kingdex == 3 and currstart[2] == "R"):
		if (currstart[1] == "B" and currstart[5] == "Q" and currstart[0] != "B"):
			maincounter += 1
			print(currstart)
			continue
	# Make sure that there's a bishop on at least one side of the king. Required for all cases.
	if (currstart[kingdex - 1] != "B" and currstart[kingdex + 1] != "B"):
		othercounter += 1
		# print(currstart)
		continue
	# Special case if the king is on C. Has some special defender checks and a check to see if there is a queen on F and bishop on B.
	if (kingdex == 2):
		if (currstart[5] == "Q" and currstart[1] == "B"):
			maincounter += 1
			print(currstart)
			continue
		elif (currstart[1] == "Q" and currstart[3] == "B"):
			if (currstart[kingdex + 2] == "B" or currstart[kingdex + 2] == "Q" or currstart[kingdex + 3] == "N" or currstart[kingdex - 1] == "N" or currstart[5] == "N"):
				othercounter += 1
				# print(currstart)
				continue
			else:
				maincounter += 1
				print(currstart)
				continue
		else:
			othercounter += 1
			# print(currstart)
			continue
	# Special case if the king is on F, similar to the above.
	if (kingdex == 5):
		if (currstart[2] == "Q" and currstart[6] == "B"):
			maincounter += 1
			print(currstart)
			continue
		elif (currstart[4] == "B" and currstart[6] == "Q"):
			if (currstart[kingdex - 2] == "B" or currstart[kingdex - 2] == "Q" or currstart[kingdex - 3] == "N" or currstart[kingdex + 1] == "N" or currstart[2] == "N"):
				othercounter += 1
				# print(currstart)
				continue
			else:
				maincounter +=1
				print(currstart)
				continue
		else:
			othercounter += 1
			# print(currstart)
			continue
	# "Normal" defender checks; basically repeated above because I'm a lazy shit
	if (currstart[kingdex + 1] == "B"):
		if (currstart[kingdex + 2] == "B" or currstart[kingdex + 2] == "Q" or currstart[kingdex + 3] == "N" or currstart[kingdex - 1] == "N"):
			othercounter += 1
			# print(currstart)
			continue
	else:
		if (currstart[kingdex - 2] == "B" or currstart[kingdex - 2] == "Q" or currstart[kingdex - 3] == "N" or currstart[kingdex + 1] == "N"):
			othercounter += 1
			# print(currstart)
			continue
	# Fool's mate is impossible if the king is on B or G
	if (kingdex == 1 or kingdex == 6):
		othercounter += 1
		# print(currstart)
		continue
	# Case to deal with the king being on E
	if (kingdex == 4):
		if (currstart[5] == "B"):
			if (currstart[3] == "Q" or currstart[1] == "Q"):
				maincounter += 1
				print(currstart)
				continue
			else:
				othercounter += 1
				# print(currstart)
				continue
		if (currstart[3] == "B"):
			if (currstart[5] == "Q" or currstart[7] == "Q"):
				maincounter += 1
				print(currstart)
				continue
			else:
				othercounter += 1
				# print(currstart)
				continue
		else:
			othercounter += 1
			# print(currstart)
			continue
	# Case to deal with the king being on D; hopefully this should only occur if nothing above it occurs
	else:
		if (currstart[4] == "B"):
			if (currstart[2] == "Q" or currstart[0] == "Q"):
				maincounter += 1
				print(currstart)
				continue
			else:
				othercounter += 1
				# print(currstart)
				continue
		if (currstart[2] == "B"):
			if (currstart[4] == "Q" or currstart[6] == "Q"):
				maincounter += 1
				print(currstart)
				continue
			else:
				othercounter += 1
				# print(currstart)
				continue
		else:
			othercounter += 1
			# print(currstart)
			continue
	# Old and mostly useless code?
	# left = (currstart[kingdex - 1] == "R" or currstart[kingdex - 1] == "Q" or currstart[kingdex - 2] == "B" or currstart[kingdex - 2] == "Q" or currstart[kingdex - 3] == "N")
	# right = (currstart[kingdex + 1] == "R" or currstart[kingdex + 1] == "Q" or currstart[kingdex + 2] == "B" or currstart[kingdex + 2] == "Q" or currstart[kingdex + 3] == "N")
	# both = (currstart[kingdex + 1] == "N" or currstart[kingdex - 1] == "N")
	# Case when both of the sides are protected; this means that the fool's mate is impossible and we continue to the next setup.
	# if ((left and right) or both):
	# 	continue
	# Case when both of the sides are unprotected; this means that the fool's mate is always possible (except in a few edge cases that we account for later) and we add one to the counter.
	# elif (!(currstart[kingdex - 1] == "R" or currstart[kingdex - 1] == "Q" or currstart[kingdex - 2] == "B" or currstart[kingdex - 2] == "Q" or currstart[kingdex - 3] == "N")
	# and !(currstart[kingdex + 1] == "R" or currstart[kingdex + 1] == "Q" or currstart[kingdex + 2] == "B" or currstart[kingdex + 2] == "Q" or currstart[kingdex + 3] == "N")):
	# 	counter += 1
	# 	continue
	# Case when two angles of attack are possible; can happen if (the king is between C and F AND there is a bishop or queen on its mirror square) OR (the bishop and the queen are on opposite sides of the board and both are valid)
	# elif ((kingdex in range(2, 6)) and (currstart[foo(kingdex)] == "B" or currstart[foo(kingdex)] == "Q")) or
	# ((("Q" in currstart[1:4] and "B" in currstart[4:7]) or ("Q" in currstart[4:7] and "B" in currstart[1:4])) and ((queendex % 2 != kingdex % 2) and bishopvalid(currstart)):
	# 	if (!(currstart[kingdex - 1] == "R" or currstart[kingdex - 1] == "Q" or currstart[kingdex - 2] == "B" or currstart[kingdex - 2] == "Q" or currstart[kingdex - 3] == "N")
	# 	or !(currstart[kingdex + 1] == "R" or currstart[kingdex + 1] == "Q" or currstart[kingdex + 2] == "B" or currstart[kingdex + 2] == "Q" or currstart[kingdex + 3] == "N")):
	# 		counter += 1
	# 		continue
	# Case where only one angle of attack is possible
	# else:
		# Find out the attacking piece and their index
		# attackdex =
		# Find out which angle is being attacked

		# Find out if that angle is defended

# Find out what we ended up with
print(maincounter)
print(othercounter)
