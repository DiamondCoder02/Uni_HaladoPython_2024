# -------------------------------------------------------
# Kovács Dániel Márk - KO8LM4
# -------------------------------------------------------

# This is just to clear the console
# https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
from calendar import c
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
		# store the number and start from 2
		self.n = n
		self.current = 2
		self.primes=[]

	# iterator returns itself as an iterator object
	def __iter__(self):
		return self

	def __next__(self):
		# if the current number is greater or equal to the number we want to check, we stop
		while True:
			if self.current >= self.n:
				# Thank you github copilot for explaining raise and StopIteration
				raise StopIteration # GC: "StopIteration is a built-in exception in Python that is primarily used to signal the end of an iterator"
			else : # if the number is prime, return it
				if self.isPrime(self.current):
					# store the prime number
					primeNum = self.current
					# increment the current number
					self.current += 1
					# append the prime number to the list
					self.primes.append(primeNum)
					# return the prime number
					return primeNum
				else:
					# if it's not prime, increment the current number
					self.current += 1

	def isPrime(self, n):
		# 2 and 3 are prime numbers
		if n == 2 or n == 3: return True
		# even numbers and negatives are not prime
		if n % 2 == 0 or n < 2: return False
		# check if the number is divisible by any prime number
		for prime in self.primes:
			# if the number is divisible by a prime number, it's not prime
			if n % prime == 0:
				return False
		return True


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

def primeCalc(n):
	# 2 and 3 are prime numbers
	if n == 2 or n == 3: return True  
	# even numbers and negatives are not prime
	if n % 2 == 0 or n < 2: return False
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
		# Matrix size
		self.size = size
		# create a matrix with random numbers
		self.matrix=[[random.randint(0,2)for i in range(size)]for j in range(size)]
	
	def __iter__(self):
		# row and column counters
		self.current_row = 0 
		self.current_col = 0
		return self

	def __next__(self):
		# if the row is less than the size, create a row
		if self.current_row < self.size:
			# get the value from the matrix
			value = self.matrix[self.current_row][self.current_col]
			# increment the column
			self.current_col += 1
			# if the column is equal to the size, increment the row and reset the column
			if self.current_col == self.size:
				self.current_row += 1
				self.current_col = 0
			# return the value
			return value
		else:
			# if the row is greater than the size, stop
			raise StopIteration

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
# This is the stupidest thing I've ever seen in any programming language. My head can't comprehend this.
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
# Challenge 5 (Last)
# -------------------------------------------------------
# Write a Python function that converts a given phone number 
# Format: "(+36) 30 123 4567"
# The input phone number can only contain digits.
# ??? Use regex to validate the phone number ???
# https://en.wikipedia.org/wiki/Telephone_numbers_in_Hungary

import re

@Logger
def phone_number():
	# ask for a phone number and strip it
	phoneNum = input("Enter a phone number: ").strip()
	# check if the phone number is valid with my own bad function
	if noRegexPhone(phoneNum):
		print("Valid hungarian phone number")
		# print and convert the phone number
		print(convertPhoneToReadeableFormat(phoneNum))
	else:
		print("Invalid phone number. Won't convert. LOL")
	pass

# Possible phone numbers:
# 06 30 123 4567
# 36 30 1234 567
# 06301234567

# Rules:
# The input number can start only with 06 or 36
# Then digits can be 20, 30, 70, 1
# Then 7 digits can be any number

@Logger
def convertPhoneToReadeableFormat(phoneNumber):
	# check if the phone number is valid
	pattern = re.compile(r"(\+\d(06|36))?\s?\(?\d(20|30|70|1)\)?[\s.-]?\d{3}[\s.-]?\d{4}")
	# check if the phone number matches the pattern
	match = re.search(pattern, phoneNumber)
	if match:
		# remove any non-digit characters
		phoneNumber = re.sub(r"\D", "", phoneNumber)
		# check if the phone number starts with 06 or 36
		phoneNumber = re.sub(r"^(06|36)", r"(+36) ", phoneNumber)
		# add spaces between the numbers
		phoneNumber = re.sub(r"(\d{2})(\d{3})(\d{4})", r"\1 \2 \3", phoneNumber)
		# return the phone number
		return phoneNumber
	else:
		return "Not a valid phone number. Can't convert."

@Logger
def noRegexPhone(phoneNumber):
	# check if it has spaces
	if " " in phoneNumber:
		# remove the spaces
		phoneNumber = phoneNumber.replace(" ", "")
	# check if it has brackets
	if "(" in phoneNumber:
		# remove the brackets
		phoneNumber = phoneNumber.replace("(", "")
		phoneNumber = phoneNumber.replace(")", "")
	# check if it has a plus
	if "+" in phoneNumber:
		# remove the plus
		phoneNumber = phoneNumber.replace("+", "")
	# remove any other characters that are not digits
	phoneNumber = re.sub(r"\D", "", phoneNumber)
	# check if it has 06 or 36 at the start
	if phoneNumber.startswith("06") or phoneNumber.startswith("36"):
		# if it has 06, replace it with 36
		if phoneNumber.startswith("06"):
			phoneNumber = phoneNumber.replace("06", "36")
	else:
		phoneNumber = "36" + phoneNumber
	# check if the length is 11
	if len(phoneNumber) != 11:
		return False
	# check if the first number is 20, 30, 70
	if phoneNumber[2] not in ["2", "3", "7"]:
		return False
	if phoneNumber[3] not in ["0"]:
		return False
	# check if the rest of the numbers are digits
	if not phoneNumber[3:].isdigit():
		return False
	# print(phoneNumber)
	return True





# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# This is the start of the program
# -------------------------------------------------------
# -------------------------------------------------------
# Kovács Dániel Márk - KO8LM4
# -------------------------------------------------------

# If this fires, the first challenge is working
@Logger
def start():
    # I have a fetish for making menus so...
    # I hope no comment really needed ^^'
	print("Welcome, choose which challenge you wanna test:")
	print("0. Exit \n"
		"1. Logger decorator with logs \n"
		"2. Prime numbers with iterators, generators \n"
		"3. n*n matrix \n"
		"4. Class atrribute with initial value \n"
		"5. Phone number validation"
	)

	# Just choose a "number" string to test the challenges
	menuChoice = input("Choose a number: ").strip()
	if menuChoice == "1":
		cls()
		test()
	elif menuChoice == "2":
		cls()
		is_prime()
	elif menuChoice == "3":
		cls()
		matrix_generator()
	elif menuChoice == "4":
		cls()
		descriptor_class()
	elif menuChoice == "5":
		cls()
		phone_number()
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

# -------------------------------------------------------
# Kovács Dániel Márk - KO8LM4
# -------------------------------------------------------