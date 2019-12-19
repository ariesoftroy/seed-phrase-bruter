# Bruteforce (this one need a lots of processing power)
# 24 words usually written on pieces of paper (SEED PHRASES)
# that forensic analyst almost always find 
# in crypto criminal apartments and rooms :)
import itertools


words = []

for x in range(24):
	print("Insert the word: ")
	w = input()
	words.append(w)
	pass
print(words)

for i in itertools.permutations(words):
	print(i)	
	pass
