#mainDice.py

import random as rd
import matplotlib as mtp
import pickle as pl
import numpy as np
from PIL import Image
import math


#TODO: determine if this method for generating dice is truly random, or at the very least equivalent to the method Dr. Gowers suggested

def generate1(n):

	die = []

	stan = list(range(1, n + 1, 1))
	die = stan

	for i in range(500):
		
		x = rd.randint(0, n - 1)
		y = rd.randint(0, n - 1)		

		if die[x] <= 1 or die[y] >= n:
			continue
		else:
			die[x] -= 1
			die[y] += 1

	die.sort()

	return die

def generate(num, n):

	dice = []
	count = 0

	while len(dice) < num:
		
		count += 1

		die = [rd.randint(1, n) for i in range(n)]
		if sum(die) != (n * (n + 1)) / 2:
			continue
		die.sort()
		dice.append(die)

	print "Count: " + str(count)

	return dice


#dom function

def dom(a, b, n):

	adom = 0
	bdom = 0

	for i in range(n):
		for j in range(n):
			
			if a[i] > b[j]:
				adom += 1
			elif a[i] < b[j]:
				bdom += 1
			else:
				continue
	
	if adom > bdom:
		return "Beats"
	elif adom < bdom:
		return "Loses"
	else:
		return "Ties"


def initgen():

	n = 300
	maindie = generate(1000, n)
	
	of = open("example.p", "wb")
	pl.dump(maindie, of)
	of.close()

	return 0

def testgen():
	
	infile = open("s300x1000.p", "rb")
	maindie = pl.load(infile)
	infile.close()
	print maindie


def calc_result():

	n = 300
	x = 1000	

	infile = open("s300x1000.p", "rb")
	dice = pl.load(infile)
	infile.close()

	results = [[0 for i in range(x)] for j in range(x)]
	
	for i in range(x):
		for j in range(x):
			results[i][j] = dom(dice[i], dice[j], n)

	ofile = open("results_s300x1s000_1.p", "wb")
	pl.dump(results, ofile)
	ofile.close()

	return 0

def test_res():

	infile = open("results_s300x1000_1.p", "rb")
	result = pl.load(infile)
	infile.close()

	print result


	return 0

def plot_result():

	n = 300
	x = 1000

	infile = open("results_s300x1000_1.p", "rb")
	result = pl.load(infile)
	infile.close()

	plt = np.zeros((x, x, 3))
	red = np.array([255, 0, 0])
	green = np.array([0, 0, 255])

	win_per = [] 
	

	for i in range(x):
		for j in range(x):
			if result[i][j] == "Loses":
				plt[i][j] = red
			elif result[i][j] == "Beats":
				plt[i][j] = green


	plt_im = Image.fromarray(np.uint8(plt), "RGB")
	#plt_im.show()	
	plt_im.save("results_image_s300x1000_1.png", "PNG")

	for i in range(x):
		runwin = 0
		for j in range(x):	
			if result[i][j] == "Beats":
				runwin += 1
		win_per.append(float(runwin) / x)

	print win_per

	win_per = np.array(win_per)
	
	print "Mean: " + str(win_per.mean())
	print "Var: " + str(win_per.var())

	return 0
		

#testgen()
#initgen()
#main()
#test_res()
plot_result()
