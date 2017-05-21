import random as rd
import matplotlib.pyplot as mtp
import pickle as pl
import numpy as np
from PIL import Image
import math
import time
import testGen



def stanDist(die, n):

	stan = range(1, n + 1, 1)
	dist = 0
	for i in range(n):
		dist += abs(die[i] - stan[i])

	#print(dist)

	return dist

def dieDist(die1, die2, n):

	dist = 0
	for i in range(n):
		dist += abs(die1[i] - die2[i])

	#print(dist)

	return dist




#Picks out dice with distance of 30, 312, and 2450 to match P Peng's test
#Won't work if he's using the unconstrained sum model. I'll match the test under constrained sum
def pickVar():

	n = 100
	testDice = []

	foundIt = False
	while (not foundIt):
		die = testGen.generate_pips(n, int(n * math.log(n, 2)))
		#print(die)
		#time.sleep(1)
		x = stanDist(die, n)
		if x < 70:
			foundIt = True

	testDice.append(die)

	print("Found < 70")

	foundIt = False
	while (not foundIt):
		die = testGen.generate_pips(n, int(n * math.log(n, 2)))
		x = stanDist(die, n)
		if x > 190 and x < 210:
			foundIt = True

	testDice.append(die)
  
	print("Found ~200")

	foundIt = False
	while (not foundIt):
		die = testGen.generate_pips(n, int(n * math.log(n, 2)))
		x = stanDist(die, n)
		if x > 650:
			foundIt = True

	testDice.append(die)

	print("Found > 650")

	ofile = open("testDice_100s_70_200_650.p", "wb")
	pl.dump(testDice, ofile)
	ofile.close()




#After generating 1M dice with 100 sides, we have a standard distance minimum of 52, max of 702 and mean of 200
def main():

	n = 100

	distL = []

	for i in range(1000000):
		if i % 1000 == 0:
			print i
		die = testGen.generate_pips(n, int(n * math.log(n, 2)))
		x = stanDist(die, n)
		distL.append(x)

	distL = np.array(distL)
	print "Min: " + str(distL.min())
	print "Max: " + str(distL.max())
	print "Mean: " + str(distL.mean())

	return 0

def main2():


	n = 100

	infile = open("testDice_100s_70_200_650.p", "rb")
	dice = pl.load(infile)
	infile.close()
	
	distL = [[], [], []]

		
	for i in range(100000):
		if i % 1000 == 0:
			print i

		newDie = testGen.generate_pips(100, int(n * math.log(n, 2)))

		distL[0].append(dieDist(dice[0], newDie, n))
		distL[1].append(dieDist(dice[1], newDie, n))
		distL[2].append(dieDist(dice[2], newDie, n))
		
		#print(distL)
		#time.sleep(1)

	ofile = open("results_testDice_100s_70_200_650.p", "wb")
	pl.dump(distL, ofile)
	ofile.close()


	return 0

def plotResult():

	n = 100

	infile = open("results_testDice_100s_70_200_650.p", "rb")
	res = pl.load(infile)
	infile.close()

	histos = [{}, {}, {}]

	#Maximum distance achieved in any test
	for i in range(1285):
		histos[0][i] = 0
		histos[1][i] = 0
		histos[2][i] = 0

	for j in range(len(histos)):
		for i in range(len(res[j])):
			histos[j][res[j][i]] += 1

	ult = max(len(histos[0]), len(histos[1]), len(histos[2]))

#	print(ult)
#	print(len(histos[0].values()))

	#plot(range(min(res[0]), max(res[0]) + 1), histo 

	fig = mtp.figure()
	fig.suptitle("Dice Distance, Sum Constrained Case", fontsize = 16)
 
	mtp.bar(range(ult), histos[0].values(), align = 'center', color = 'red')
	mtp.xticks(range(ult), histos[0].keys())
	mtp.bar(range(ult), histos[1].values(), align = 'center', color = 'blue')
	mtp.xticks(range(ult), histos[1].keys())
	mtp.bar(range(ult), histos[2].values(), align = 'center', color = 'green')
	mtp.xticks(range(ult), histos[2].keys())

#	leg = mtp.legend(('red', 'blue', 'green'), ("70", "200", "650"))

	mtp.savefig('results_testDice_100s_70_200_650.png')
	




#main()
#pickVar()
#main2()
plotResult()
