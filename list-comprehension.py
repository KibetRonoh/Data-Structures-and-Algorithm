# List comprehension
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)


even_squares = [x ** 2 for x in range(1, 30) if x % 2 == 0]
print(even_squares)

# Alternatively
# for understanding, above generation is same as,
odd_square1 = []
 

 
print(odd_square1)



# Python program to demonstrate list comprehension in Python

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print (odd_square)

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x**2)
print (odd_square)

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print (power_of_2)

# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print (primes)

# list for lowering the characters
print ([x.lower() for x in ["A","B","C"]] )

# list which extracts number
string = "my phone number is : 11122 !!"

print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print (numbers)

# A list of list for multiplication table
a = 5
c = 4
table = [[a, b, c, a * b * c] for b in range(1, 11)]

print("\nMultiplication Table")
for i in table:
	print (i)


###############################################################################
# Python program to print 3D list
# importing pretty printed
import pprint
  
def ThreeD(a, b, c):
    lst = [[ ['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return lst
      
# Driver Code
col1 = 5
col2 = 3
row = 2
# used the pretty printed function
pprint.pprint(ThreeD(col1, col2, row))


##################################################
matrix = []

for i in range(5):
	
	# Append an empty sublist inside the list
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print(matrix)

###################
# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(5)]

print(matrix)


#######################################################

# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flatten_matrix = []

for sublist in matrix:
	for val in sublist:
		flatten_matrix.append(val)
		
print(flatten_matrix)
#############

# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]

print(flatten_matrix)

############################################################


# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

flatten_planets = []

for sublist in planets:
	for planet in sublist:
		
		if len(planet) < 6:
			flatten_planets.append(planet)
		
print(flatten_planets)
####################

# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

# Nested List comprehension with an if condition
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]
		
print(flatten_planets)

#######################################################################