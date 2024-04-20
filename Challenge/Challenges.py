# This is just to clear the console
# https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



# -------------------------------------------------------
# Challenge 1
# -------------------------------------------------------
# Write a logger decorator function, that logs, which function is called, which module it is called from, when was it called.
# The logged informations should be written to a file, named functionCalls.log.
# Example: Function 'example_funciont' was called from module '__main__' at 2021-01-01 12:00:00

# A quick tip: inspect

from datetime import datetime

class Logger:
    # With the __init__ method we can pass the function to the decorator
	def __init__(self, func):
		# we store the function in the class
		self.func = func
	
	# With this we can call the function and log the information
	def __call__(self, *args, **kwargs):
		# we don't need the count, we just need the current time
		time = datetime.now()
		# we open the file in append mode, so we don't overwrite the previous logs
		with open("functionCalls.log", "a") as file:
			# we write the information to the file
			file.write(f"Function '{self.func.__name__}' was called from module '{__name__}' at '{time}'\n")
		# we return the function itself
		return self.func(*args, **kwargs)

# Below this is just to test multiple runs of the same function
# and to test the decorator itself
@Logger
def	test(): 
	print("Hello from logger_decorator")
	for i in range(5):
		loopThisIfNeeded()
	pass

@Logger
def loopThisIfNeeded():
	print("Hello from loopThisIfNeeded")
	pass



# -------------------------------------------------------
# -------------------------------------------------------
# Challenge 2
# -------------------------------------------------------
# With iterators and generators in a given range, 
# find all the prime numbers and print them out.

@Logger
def is_prime():
    # ask for a number
	number = int(input("Enter a number for the iterator: "))
	# create an instance of the PrimeNumbers class
	prime = PrimeNumbersIter(number)
	# iterate through the prime numbers
	for i in prime:
		# print
		print(i)
	pass

	number2 = int(input("Enter a number for the generator: "))
	for i in prime_generator(number2):
		print(i)

# logger
@Logger
class PrimeNumbersIter:
	def __init__(self, n):
		# store the number and start from 1
		self.n = n
		self.current = 1

	# iterator returns itself as an iterator object
	def __iter__(self):
		return self

	def __next__(self):
		# if the current number is greater or equal to the number we want to check, we stop
		self.current += 1
		while True:
			if self.current >= self.n:
				# Thank you github copilot for explaining yield and StopIteration
				yield StopIteration # GC: "StopIteration is a built-in exception in Python that is primarily used to signal the end of an iterator"
			else : # if the number is prime, return it
				if self.prime(self.current):
					primeNum = self.current
					self.current += 1
					return primeNum
				else:
					# if it's not prime, call the function again
					return self.__next__()

	# check if the number is prime
	def prime(self, num):
		return primeCalc(num)


@Logger
def prime_generator(max_value):
	current = 1
	# Just loop through the numbers
	while current < max_value:
		# if the number is prime, yield it
		if primeCalc(current):
			# GC: When a yield is called, it returns a generator object without beginning execution of a function.
			yield current
		current += 1

@Logger
def primeCalc(n):
	# 2 and 3 are prime numbers
	if n == 2 or n == 3: return True  
	# even numbers and negatives are not prime
	if n % 2 == 0 or n < 3: return False
	# check if the number is divisible by any odd number
	for i in range(3, int(n ** 0.5) + 1, 2):  # class range(start, stop, step)
		# if it is, it's not prime
		if n % i == 0:
			return False
	# if it's not divisible, it's prime
	return True



# -------------------------------------------------------
# -------------------------------------------------------
# Challenge 3 (2 points?)
# -------------------------------------------------------
# create a class, that when instantiation it gives back an 
# n*n matrix (n should be an attribute of the class), filled with
# 0, 1 and 2 values randomly.

# write it in different ways:
# You cannot put a method in the class that generates the matrix.

import random

@Logger
class MatrixMagic:
	def __init__(self, size):
		self.size = size # Matrix size
		self.current_row = 0 
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.current_row >= self.size:
			raise StopIteration
		else:
			self.current_row += 1
			return self.matrix[self.current_row - 1]

	# The @property decorator used to define methods in a class that are intended to be accessed like attributes, 
	# 	without needing to call them as a method with parentheses.
	@property # Decorator that makes the method a property
	def matrix(self):
		# create a list of lists
		matrix = []
		# loop through the size
		for i in range(self.size):
			# create a list of random numbers
			matrix.append([random.randint(0, 2) for i in range(self.size)])
		# return the matrix
		return matrix

class MatrixMagic2:
	def __init__(self, size):
		self.size = size # Matrix size
		self.row2 = 0 # row counter
	
	def __iter__(self):
		return self

	# The __next__ method is called to get the next item in the iterator
	def __next__(self):
		# if the row is less than the size, create a row
		if self.row2 < self.size:
			# create a row of random numbers
			row = [random.randint(0, 2) for i in range(self.size)]
			# increment the row
			self.row2 += 1
			return row
		else:
			# if the row is greater than the size, stop
			raise StopIteration

@Logger
def matrix_generator():
	# ask for a number
	number = int(input("Enter a number for the matrix: "))
	# create an instance of the MatrixMagic class
	matrix = MatrixMagic(number)
	print("Matrix with property:")
	# print the matrix
	for i in matrix.matrix:
		print(i)
	print("------")

	# create an instance of the MatrixMagic2 class
	matrix2 = MatrixMagic2(number)
	print("Matrix with generator:")
	for i in matrix2:
		print(i)
	print("------")
	pass



# -------------------------------------------------------
# -------------------------------------------------------
# Challenge 4 
# -------------------------------------------------------
# Create a class that has one atrribute that has an initial value.
# With descriptor class make it only possible to edit if the new value is greater than the initial value.

@Logger
class AtrributeThings:
	def __init__(self, numb = 0):
		self.numb = numb

	# instance is the instance of the class, owner is the class itself
	def __get__(self, instance, owner): 
		# if the value is set, return that, if not, return the initial value
		return instance.__dict__.get('setNum', self.numb)

	def __set__(self, instance, value): # value is the new value
		# if the value is greater than the setNum value in the dictionary, set it
		if value > instance.__dict__.get('setNum', self.numb):
			# set that dictionary value to the new value
			instance.__dict__['setNum'] = value
		else:
			# if not, print a message
			print(f"The number {value} is small. Give number greater than " + str(instance.__dict__.get('setNum', self.numb)) + "!")

# "To use the descriptor, it must be stored as a class variable in another class:"
# https://docs.python.org/3/howto/descriptor.html#primer
# This is the stupidest thing I've ever seen in any language. My head can't comprehend this.
@Logger
class IHateAttributes:
    # create an instance of the AtrributeThings class
    setNum = AtrributeThings(1) # The '1' is the initial value

def descriptor_class():
    # create an instance of the class
	intig = IHateAttributes() 
	print("Give a number, 0 to exit")
	while True:	
		if infinityThing(intig) == False: 
			break 
		pass

	print("------")
	pass

def infinityThing(intig):
	# ask for a number
	number = int(input(f"Current: {intig.setNum}. Choose a bigger number: ").strip())
	# if the number is 0, return False to exit the loop
	if number == 0: 
		return False
	intig.setNum = number

# Small note: I hate the internet.
# I had to ask Github Copilot 
# Q:  "how can I get a value from instance.__dict__ ?"
# GC: "... If the attribute does not exist, this will raise a 'KeyError'. 
# 		To avoid this, you can use the 'get' method of the dictionary, 
# 		which returns 'None' if the key does not exist..."



# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# This is the start of the program
# -------------------------------------------------------
# -------------------------------------------------------

# If this fires, the first challenge is working
@Logger
def start():
    # I have a fetish for making menus so...
    # I hope no comment really needed ^^'
	print("Welcome, choose which challenge you wanna test:")
	print("0. Exit \n"+
		"1. Logger decorator with logs \n"+
		"2. Prime numbers with iterators, generators \n"+
		"3. n*n matrix \n"+
		"4. Class atrribute with initial value")

	# Just choose a "number" string to test the challenges
	menuChoice = input("Choose a number: ").strip()
	if menuChoice == "1":
		cls()
		test()
	elif menuChoice == "2":
		cls()
		is_prime() # Fix this
	elif menuChoice == "3":
		cls()
		matrix_generator() # TODO a
	elif menuChoice == "4":
		cls()
		descriptor_class()
	elif menuChoice == "0":
		cls()
		print("Goodbye!")
		return False
	else:
		print("Choose a valid number!")
	pass

# Loop the start program till the user exits
while True:	
    if start() == False: 
        break 
    pass