#mainDice.py

import random as rd
import matplotlib as mtp
import pickle as pl
import numpy as np
from PIL import Image
import math
from diceFuncs import *

#Per Kent Morrison's comment, a tournament graph has a 4-cycle iff the out-degrees are 2, 2, 1, 1

def intrans_ncheck4(dice, n):

	x = len(dice)
	
	#result matrix

	result = [[0 for i in range(4)] for j in range(4)]

	tieCount = 0

	for i in range(4):
		for j in range(4):
			calc = dom(dice[i], dice[j], n)
			if (calc) == "Beats":	
				result[i][j] = 1
			elif (calc == "Ties") and j < i: #j < i lets us choose just the left side of the graph so we don't count ties twice
				tieCount += 1

	

	dice_wins = [0 for i in range(4)]
	for i in range(4):
		dice_wins[i] = sum(result[i])
	
	dice_wins.sort()

	if dice_wins == [1, 1, 2, 2]:
		return "Intrans"
	return "Trans"



def main():

	x = 4
	n = 50
	numTies = 0
	intrans = 0

	for i in range(1000):
		dice = generate(x, n)
		






	return 0







main()


