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
	prime = PrimeNumbers(number)
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
class PrimeNumbers:
	def __init__(self, n):
		# store the number and start from 1
		self.n = n
		self.current = 1

	# iterator
	def __iter__(self):
		return self

	def __next__(self):
		# if the current number is greater or equal to the number we want to check, we stop
		self.current += 1
		if self.current >= self.n:
			# Thank you github copilot for explaining yield and StopIteration
			yield StopIteration
		# if the number is prime, return it
		if self.prime(self.current):
			return self.current
		else:
			# if it's not prime, call the function again
			return self.__next__()

	# check if the number is prime
	def prime(self, num):
		# if even, it's not prime
		if num < 2:
			return False
		# now we check if it's divisible by any number
		for i in range(2, num):
			# if it's divisible, it's not prime
			if num % i == 0:
				return False
		return True

@Logger
def prime_generator(max_value):
	current = 1
	# Just loop through the numbers
	while current < max_value:
		# if the number is prime, yield it
		if primeCalc(current):
			yield current
		current += 1

@Logger
def primeCalc(n):
	# 2 and 3 are prime numbers
	if n == 2 or n == 3: return True  
	# even numbers and negatives are not prime
	if n % 2 == 0 or n < 2: return False
	# check if the number is divisible by any odd number
	for i in range(3, int(n ** 0.5) + 1, 2):  
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

def matrix_generator():
	pass










# -------------------------------------------------------
# -------------------------------------------------------
# Challenge 4 
# -------------------------------------------------------
# Create a class that has one atrribute that has an initial value.
# With descriptor class make it only possible to edit if the new value is greater than the initial value.

def descriptor_class():
	# create an instance of the class
	instance = AtrributeThings()
	print(instance.value)
	# set the value to 5
	instance.value = 5
	print(instance.value)
	# try to set it to 3
	instance.value = 3
	print(instance.value)
	# try to set it to 6
	instance.value = 6
	print(instance.value)
	
    
	pass

@Logger
class AtrributeThings:
	def __init__(self, value = 1):
		self.value = value

	def __get__(self, instance):
		return instance.__dict__.get('value', self.value)

	def __set__(self, instance, setting):
		if setting > instance.__dict__.get('value', self.value):
			instance.__dict__['value'] = setting
		else:
			print("Give me number greater than the " + str(instance.__dict__.get('value', self.value)) + "!")
		pass










# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# This is the start of the program
# -------------------------------------------------------
# -------------------------------------------------------

# This is just to clear the console
# https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
		matrix_generator()
	elif menuChoice == "4":
		cls()
		descriptor_class() # Fix this
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