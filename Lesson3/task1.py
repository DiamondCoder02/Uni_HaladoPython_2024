# Nested function calls

import random

def greeting(name):
	def inner_greet():
		print(f"Hello, {name}!")
	inner_greet()

greeting("John")

def greetings(name):
	def inner_greetings():
		return f"Hello, {name}!"
	# inner_greetings()
	# return inner_greetings
	return inner_greetings()

print(greetings("Helen"))

print('------------------------')

def add(x:'integer number' = 10):
	"""_summary_
	Args:
		x (integer number, optional): _description_. Defaults to 10.
	"""
	def inner_add(y):
		return x + y
	return inner_add

sum = add(20) # x=20
print(type(sum))
print(sum(10)) # y=10 (Inner function call)

print(add.__doc__)
print(add.__annotations__)
print(add.__defaults__)

print('------------------------')

# Higher order functions

def factor(n):
    if n <= 1:
        return n
    else:
        return n * factor(n-1)

# print(factor(5))

def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def print_recursion(func, n):
	for i in range(n):
		print(f"{i}. {func(i)}")

print_recursion(factor, 10)
print('------------------------')
print_recursion(fibonacci, 20)

print('------------------------')

def even_numbers(num):
	if num % 2 == 0:
		return num

def odd_numbers(num):
	if num % 2 != 0:
		return num

def all_numbers(num):
	return num

def list_generator(n, value1, value2, func):
	my_list = []
	while len(my_list) < n:
		number = random.randint(value1, value2)
		if func(number):
			my_list.append(func(number))
	return my_list

print(list_generator(10, 1, 200, even_numbers))
# print(list_generator(15, 30, 313, odd_numbers))

print('------------------------')

# Lambda functions

square = lambda x: x**2
print(type(square))
print(square(5))

string_back = lambda s: s[::-1] # Reverse stringS
print(string_back("Hello, I'm gay and so are you"))
print(string_back("Géza kék az ég"))

print('------------------------')

# Lambda functions, with parameters

def apply_func(fn, *args):
	return fn(*args)

print(apply_func(lambda x, y: x**y, 5,3))
# print(apply_func(lambda *args: sum(args), 3,4,5,6,7,8,9))
# Error

print('------------------------')

# Lambda and sorting

s = ["B", "c", 'R', 't', "K", 'l']
print(sorted(s))
print(ord("a"))
print(ord("b"))
print(ord("A"))
print(ord("B"))
print(ord("ß"))
print(ord("🔞"))
print(sorted(s, key=lambda c: c.upper()))

print('------------------------')

words = ["apple", "banana", "durian", "elderberry", "fig", "grape"]
print(sorted(words, key=lambda x: len(x)))

my_string = "This is a very interesting string for the lambda function."
result_words = lambda x: len(x.split())
print(my_string," = ", result_words(my_string), "words")

my_string2 = "You can also use it like this"
result_words2 = (lambda x: len(x.split()))(my_string2)
print(my_string2," = ", result_words2, "words")

print('------------------------')

d = {'abc': 200, 'def': 500, 'ghi': 300}
print(sorted(d))
print(sorted(d, key = lambda x: d[x]))

print('------------------------')

# Complex numbers sorting

def dist_sq(x):
	return (x.real)**2 + (x.imag)**2

list_complex = [3+3j, 1-1j, 0, 2+0j]
# print(sorted(list_complex)) # Won't work !!!
print(sorted(list_complex, key=lambda x: (x.real)**2 + (x.imag)**2))

print('------------------------')
print('------------------------')