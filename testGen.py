import random as rd
#import matplotlib.pyplot as mtp
import pickle as pl
import numpy as np
from PIL import Image
import math
import time


def generate_pips(n, burn):

	die = []

	stan = list(range(1, n + 1, 1))
	die = stan

	for i in range(burn):
		
		a = rd.randint(1, n)

		x = rd.randint(0, n - 1)
		y = rd.randint(0, n - 1)		

		if die[x] <= a or die[y] > (n - a):
			continue
		else:
			die[x] -= a
			die[y] += a

	die.sort()

	return die
	
def main():

	x = 1000
	n = 100
	burn_notices = [n ** (.5), n, 2 * n, n**2, n ** 3]
	
	print("Starting...")

	dice = [[], [], [], [], []]
	
	
	for j in range(len(burn_notices)):
		print("Currently at... " + str(j))
		for i in range(x):
			if i % 100 == 0:
				print("\tWithin, at: " + str(i))
			dice[j].append(generate_pips(n, int(burn_notices[j])))
	
	ofile = open("burn_tests3.p", "wb")
	pl.dump(dice, ofile)
	ofile.close()

	return 0
	
def test_results():

	x = 1000
	n = 100

	infile = open("burn_tests2.p", "rb")
	dice = pl.load(infile)
	infile.close()
	
	results = [dict(), dict(), dict(), dict(), dict()]
	
	#Calculate total variation for each die from the standard die
	
	for z in range(5):
		for i in range(x):
			for j in range(n):
				item = str(dice[z][i][j])
				
				if item in results[z]:
					results[z][item] += 1
				else:
					results[z][item] = 0
			
	
		
	
	for z in range(5):
		show = np.array(list(results[z].values()))
		#print(show)
		show = show / (n * x)
		#print(show)
		
		print("Mean " + str(z) + ": " + str(show.mean()))
		print("Var " + str(z) + ": " + str(show.var()))

def test_results2():

	x = 1000
	n = 100

	infile = open("burn_tests2.p", "rb")
	dice = pl.load(infile)
	infile.close()
	
	#for i in range(len(dice[3])):
	#	print(dice[3][i])
	
	#return 
	
	results = [[], [], [], [], []]
	
	#Create the histogram for the standard die
	stan = {}
	for i in range(n):
		stan[str(i + 1)] = 1
	
	#Calculate total variation for each die from the standard die
	
	for z in range(5):
		for i in range(x):
			g = dict()
			totvar = 0
			
			#print(sum(dice[z][i]) == (n * (n + 1) / 2))
			
			#if i < 10 and z > 1:
			#	print(dice[z][i])
			
			for j in range(n):

				item = str(dice[z][i][j])
				
				#print(str(dice[z][i][j]))
				#time.sleep(1)
				
				if item in g:
					g[item] += 1
				else:
					g[item] = 1
			
			for key in stan:
				#print(g[key])
				#print(stan[key])
				#print()
				#time.sleep(1)
				if key not in g:
					ref = 0
				else:
					ref = g[key]
				#if z > 2:
					#print((ref - stan[key]))
					
				#Total Variation Distance
				totvar += (.5 * abs(ref - stan[key]))
			
			#print(totvar)
			
			results[z].append(totvar)
	
		
	for z in range(5):
		show = np.array(list(results[z]))
		
		print("Mean " + str(z) + ": " + str(show.mean()))
		print("Var " + str(z) + ": " + str(show.var()))
		
	
#	mtp.bar(range(len(results[4])), results[4].values(), align = 'center')
#	mtp.xticks(range(len(results[4])), results[4].keys())
#	mtp.show()
	
	#print(results)
	
#main()
#test_results2()
