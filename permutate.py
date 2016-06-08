#construct all permutations on a sequence.  for example, there are 24 possibilities for an array of length 4 in which each element is unique.
#first done recursively.  after that, attempts were made to permutate without recursion, with limited success.
#am able to permutate without recursion for any given size, but not generalize...very frustrating.


def rotate2(arr,b,e): #This is a helper function.  given an array and two indices rotates those indices(by 1)
	if e<b:#make it right.  the beggining should be less than the end
		x=e
		e=b
		b=x
	holdMe=arr[b]
	for i in range(b,e):
		arr[i]=arr[i+1]
	arr[e]=holdMe
	return arr


def makeString(arr):#another helper.  takes an array of letters and makes it into a proper string
	string=''
	for i in range(len(arr)):
		string+=arr[i]
	return string
	
def permutate(arr):#recursion is easiest
	solutions = []
	
	if len(arr)==3:#basecase- three is often a nice base case.
		for i in range(6):
			if (i%2):rotate2(arr,1,2)
			else:rotate2(arr,0,1)
			solutions.append(makeString(arr))

	else:#we are dealing with anything bigger than three...
		for i in range(len(arr)):
			holdMe=arr.pop(i)
			for j in permutate(arr):
				solutions.append(holdMe + j)
			arr.insert(i,holdMe)
	return solutions


def permutateFive(arr):#nonrecursive solution for an array of length 5...not sure how you would do it generally and not have it be recursive
	solutions=[]

	for i in range(5):
		rotate2(arr,0,4)
		for i in range(4):
			rotate2(arr,1,4)
			for i in range(3):
				rotate2(arr,2,4)
				for i in range(2):
					rotate2(arr,3,4)
					solutions.append(makeString(arr))

	return solutions
def permutateSeven(arr):#this works for seven...again, not sure how you would do it generally and not have it be recursive
	#I cant seem to be able to embed for loops in a while loop
	solutions=[]

	for i in range(7):#this screams for a while loop, but so far have not been able to code it.  its a strange situation because for any given number I can do a nonrecursive function to give all permutations, but I cant do a general function.  this is the only instance where thats happened to me.
		rotate2(arr,0,6)
		for i in range(6):
			rotate2(arr,1,6)
			for i in range(5):
				rotate2(arr,2,6)
				for i in range(4):
					rotate2(arr,3,6)
					for i in range(3):
						rotate2(arr,4,6)
						for i in range(2):
							rotate2(arr,5,6)
							solutions.append(makeString(arr))

	return solutions
	#notice how the about gives solutions in a similar manner to 6*5*4*3*2*1 for all the solutions

	
	
