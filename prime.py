#primes evade patterns.  but nothing can completely evade order.
#watch the squares of odd numbers not divisible by 3.  that gets a lot of them too.
import math
#past 20, there is never more than 4 primes in a space set?  NO!!
#counterexample is 101,103,107,109
#and there is also a space of ten where no primes are....201,203,207,209
#for all primes less than one million, the maximum space where no primes are is 114.
#you can always get a bigger space, but it grows FAST, and you need really big numbers.

def collapseNumber(num):#works-add the digits of the number till it is one number
#note you lose alot of information about the original number by the end...
	if num<10:
		return num
	else:
		x=0
		for i in str(num):
			x+=int(i)
	return collapseNumber(x)
def primeFactory(num):#works
	#given a number, gives the prime factorization of that number.
	#the factorization is given in an array format, so 210 is [1,1,1,1]=2*3*5*7
	if isPrime(num):
		return num#: )	
	else:
		solutionsArray,index,currentP=[],0,2
		while num!=1:
			solutionsArray.append(0)
			while not bool(num%currentP):
				num=num/currentP
				solutionsArray[index]+=1
			currentP=nextPrime(currentP)
			index+=1
		return solutionsArray

def nextPrime(num):#works-given a prime num, this function returns the next prime num
	#in point of fact given an odd number it does it but thats not really the point.
	if num==2:
		return 3
	else:
		num=num+2
		while not isOddPrime(num):
			num=num+2
	return num
	
	def isOddPrime(num):#status-works.essentially same as below, but assumes that the number in question is
#odd from teh get go
	if not bool(num%3):#alot of odd numbers are divisible by three
		return False
	else:
		i=5
		while i<math.sqrt(num)+1:
			if not bool(num%i):
				return False
			else:
				i+=2#again, technically you need only check the next prime, but that begs the point in many respects
	return True
def isPrime(num):#status-works, for non trivial
	#dont need to check past sqrt
	if not bool(num%2):
		return False#no even number is prime other than 2
	elif not bool(num%3):
		return False#that catches a lot of the rest
	else:#technically you would only need to test divisibility by prime numbers...but this works
		i=5
		while i<math.sqrt(num)+1:#you need the plus one in case the number is in fact a square..like 121
			if not bool(num%i):
				return False
			else:
				i+=2
	return True

def primus(x,y):#given a range find all the primes in that range-inclusive
#works, for non trivial.  funny how the low ones are such a headache.
	if x<2:x=2
	if x==2:
		arr.append(x)
		arr.append(x+1)
	if not x%2:x+=1

	while x<y+1:
		if isPrime(x):
			arr.append(x)#since when can you get away with not defining the intial empty array?
		x+=2

	return arr
def primesUp(n):#gives all the primes in an array up to a given number.  can do this recursively.
	if n<22:
		return [2,3,5,7,11,13,17,19]#base case
	else:
		end=math.sqrt(n)
def PrimeSquares(x):#shows the odd squares of things not divisible by three

	arr=[49,121,169,289,361,529,841]
	#these are the squares of primes, all of which end in a 1 or 9, and all of which are not divisible by 3, and all of which are not prime
	#I have proven elsewhere that any prime number squared is not divisible by 3.
def lastDigit(n): #shows the last digit of teh primes up to n.  this is
#the exact same thing as primesUp, it just shows the last digit
	#i.e.  2,3,5,7,1,3,7,9,3,9,1,7,1,3,7,3,9,1,7,1,3,9
	arr=primus(23,n)
	arr2=[]
	for i in range(len(arr)):
		arr2.append(arr[i]%10)
	return arr2
def primeSpace(n): #gives the space between the primes
	assert n>22, "choose a bigger number"
	arr=primus(23,n)
	arr2=[]
	for i in range(len(arr)-1):
		arr2.append(arr[i+1]-arr[i])
	return arr2
def findMax(arr):#simply finds the max of the array.  I know this is a built in function its just fun
	maxi=arr[0]
	for i in range(len(arr)):
		if arr[i]>maxi:
			maxi=arr[i]
	return maxi
def spaceX(n):
	arr=lastDigit(n)
	arr2=[]
	for i in range(len(arr)-1):
		arr2.append(abs(arr[i]-arr[i+1]))
	return arr2
def upDown(n):#just more fun. if last digit is more, it up, else down.
	arr=lastDigit(n)
	arr2=[]
	for i in range(len(arr)-1):
		if arr[i]<arr[i+1]:
			arr2.append('U')
		else:
			arr2.append('D')
	return arr2
def pairWisePrime(n):#finds the pairwise primes.  be careful not to overtax your computer.
	#the taxing would happen if you want to find alot of pairwise primes
	assert n>22, "choose a bigger number"
	arr=primus(23,n)
	arr2=[]
	for i in range(len(arr)-1):
		if arr[i]-arr[i+1]==-2:#the sequence of primes just goes up...
			arr2.append((arr[i],arr[i+1]))
	return arr2
	
	def pairWisePrimeThrice(n):#curtailed fun.  only three possibilities.
	assert n>22, "choose a bigger number"
	arr=primus(23,n)
	arr2=[]
	for i in range(len(arr)-1):
		if arr[i]-arr[i+1]==-2:#the sequence of primes just goes up...
			if arr[i]%10==1:
				arr2.append('A')
			elif arr[i]%10==7:
				arr2.append('B')
			elif arr[i]%10==9:
				arr2.append('C')
			else:
				arr2.append('X')#base cases has some 5's....
	return arr2
def countingABC(arr):#just counting up the A,B,C from pairWisePrimeThrice
	A,B,C=0,0,0
	for i in range(len(arr)):
		if arr[i]=='A':
			A+=1
		elif arr[i]=='B':
			B+=1
		else:
			C+=1
	return [A,B,C]
def mersennePrimes(n):  #gives the mersenne primes up to n
#mersenne primes are quite rare.  find the mersenne, then test if prime, not the other way around
	arr=[3]
	x=4
	while x-1<n:
		if isPrime(x-1):
			arr.append(x-1)
		x=2*x
	return arr

def daKinPrime(n):  #just me messing around
	#finds the primes that are one difference from a factorial.
	#works with exception of the 1...I could change the other function but rather not.
	arr=[]
	x=1
	m=1
	while x<n:
		print x
		if isPrime(x-1):
			arr.append(x-1)
		if isPrime(x+1):
			arr.append(x+1)
		m+=1
		x=x*m
	return arr

def divisors(n):#gives ordered pairs of divisors.  note this is a very primitve check on primaliry
	arr=[(1,n)]
	i=2
	while i <= math.sqrt(n):
		if n%i==0:
			arr.append((i,n/i))
		i+=1
	return arr

def numOfDivisors(n):#as an ordered pair...
	x=1
	i=2
	while i <=math.sqrt(n):
		if n%i==0:
			x+=1
		i+=1
	return x

firstFivePerfect = [6,28,496,8128,33550336]
arr=[]
def superDivisibles(n):#finds the superdivibles (first instance of a number being divisible by the most things)
	assert n>2,"make n bigger than 2"
	arr=[4,12]
	x=13
	y=3
	while len(arr)!=n:
		if numOfDivisors(x)>y:
			arr.append(x)
			y+=1
		x+=1
	return arr


#conjecture- any number with all the same digits is not prime (past two digits)
	#trivial for even digit and 5.  for 7 and9, consider n ones multiplied by 7 or 9.
	#for 3, any sum of threes is divisible by three so the whole thing is divisible by 3
	#the only thing that remains is one....ive tested it by hand up to a few million
	#works for trillions too
print collapseNumber(45764)
print primeFactory(211)
print primus(3,60)
print isPrime(3)
#h=collapseNumber(21)
#print h
#print superDivisibles(6)
#print len(divis3rs(8128))
#print primus(23,156)
#print lastDigit(156)
#print spaceX(156)
#print upDown(156)
#print pairWisePrime(156)
#print pairWisePrimeThrice(1234)
#print countingABC(pairWisePrimeThrice(1234))
#print mersennePrimes(1)
#print daKinPrime(560000000)
#count when the winner switches from A to B to C yadda yadda.  that has to happen sometime.


#so the theory is that the array above is a way to generate a random pick from four-
#or at the very least the pattern is quite hard to spot.

#the distribution of things should defy patterns- at least strictly.
#so you can come up with many random picks from infinitely different ways of looking at primes
#the utility of all of this is to defy patterns, which are the cornestone of human thought.

#pairwise.  ending digit order is (9,1),(1,3),(7,9)
#suppose there werent infinitely pairwise primes and also there are not infinitely many mersenne primes

