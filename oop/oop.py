# Python3 program to
# demonstrate instantiating
# a class
"""An Object is an instance of a Class. A class is like a blueprint while an instance
 is a copy of the class with actual values. It’s not an idea anymore, it’s an actual dog, 
 like a dog of breed pug who’s seven years old. 

 An object consists of : 

State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.

"""

class Dog:
	
	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()




####################################################################################

# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()


########################################################################## 
# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
	
# Class for Dog
class Dog:

	# Class Variable
	animal = 'dog'			

	# The init method or constructor
	def __init__(self, breed, color):
	
		# Instance Variable	
		self.breed = breed
		self.color = color	
	
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)	


##################################################################
# Python3 program to show that we can create
# instance variables inside methods
	
# Class for Dog
class Dog:
	
	# Class Variable
	animal = 'dog'	
	
	# The init method or constructor
	def __init__(self, breed):
		
		# Instance Variable
		self.breed = breed			

	# Adds an instance variable
	def setColor(self, color):
		self.color = color
	
	# Retrieves instance variable	
	def getColor(self):	
		return self.color

# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())




"""
Constructors are generally used for instantiating an object. 
The task of constructors is to initialize(assign values) to the data members of the 
class when an object of the class is created. In Python the __init__() method 
is called the constructor and is always called when an object is created.
Syntax of constructor declaration : 


def __init__(self):
    # body of the constructor
Types of constructors : 

default constructor: The default constructor is a simple constructor which doesn’t 
accept any arguments. Its definition has only one argument which is a reference to 
the instance being constructed.
parameterized constructor: constructor with parameters is known as parameterized 
constructor. The parameterized constructor takes its first argument as a reference 
to the instance being constructed known as self and the rest of the arguments are provided
 by the programmer.
"""

class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()


############################################################################
class Addition:
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()
