import numpy as np #importing numpy module NP
# we will define a function for the checker
def checker(n):
	# crearting a variable x that will be a matrix
	org = np.zeros((n, n), dtype=int)
# adding the rows and coloumns 
	org[1::2, ::2] =1
	org[::2, 1::2] =1
# printing the entire pattern
	for i in range(n):
		for j in range(n):
			print(org[i][j], end=" ")
		print()
# n value 
n = 8
checker(n) #pritning the function
