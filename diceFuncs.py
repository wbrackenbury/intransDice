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

def dom1(a, b, n):

	adom = 0
	bdom = 0

	aDie = a
	bDie = b

	aDie.sort()
	bDie.sort()

	i = 0
	j = 0

	while i < len(aDie) and j < len(aDie):
		
		if aDie[i] < bDie[j]:
			bdom += len(bDie) - j
			i += 1		
		elif bDie[j] < aDie[i]:
			adom += len(aDie) - i
			j += 1
		else:
			pass

	
	if adom > bdom:
		return "Beats"
	elif adom < bdom:
		return "Loses"
	else:
		return "Ties"


