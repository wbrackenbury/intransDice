#mainDice.py

import random as rd
import matplotlib as mtp
import pickle as pl
import numpy as np
from PIL import Image
import math
from diceFuncs import *


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

	n = 100
	x = 1000

	infile = open("s100x1000.p", "rb")
	result = pl.load(infile)
	infile.close()
	
	
	#for i in range(10):
	#	print(result[i])
	
	#return
	
	results = []
	
	#Create the histogram for the standard die
	stan = {}
	for i in range(n):
		stan[str(i + 1)] = 1
	
	for i in range(x):
		g = dict()
		totvar = 0
		for j in range(n):
			item = str(result[i][j])
			
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
		
			
			#Total Variation Distance
			totvar += (.5 * abs(ref - stan[key]))
		
		
		#print(totvar)
		
		
		results.append(totvar)
	
	
	show = np.array(list(results))
	print("Mean: " + str(show.mean()))
	print("Var: " + str(show.var()))
	
	#print(result)


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
test_res()
#plot_result()
