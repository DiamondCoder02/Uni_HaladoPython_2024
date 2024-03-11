# Iteration, generators

# Iteration
# Iteration is the process of repeating a process multiple times. 
# In programming, iteration is a way to loop through a set of data

# 2 methods:
# __iter__ - returns an iterator object, so itself
# __next__ - returns the next item in the sequence

# To stop the iteration, we can use the StopIteration exception
# This is a built-in exception that is raised when there are no more items to return

class NumberSequence:
    def __iter__(self):
        self.a = 1 # This is where we start
        return self
    
    def __next__(self):
        # x = self.a
        # self.a += 1
        # return x
        self.a += 1
        return self.a

numbers = NumberSequence()
myIteration = iter(numbers) # numbers.__iter__()
print(next(myIteration))

for i in range(10):
	print(next(myIteration), end=' ')

print(" ")
print("-----------------")

class Fib:
	def __init__(self, max):
		self.max = max

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib

fib = Fib(100)
iter_fib = iter(fib)

for i in range(12):
	print(next(iter_fib), end=' ')

print(" ")

for n in fib:
	print(n, end=' ')

print(" ")
print("-----------------")

class EmployeeIteration:
	def __init__(self, employees):
		self.employees = employees
		self.index = 0
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.employees):
			raise StopIteration
		employee = self.employees[self.index]
		self.index += 1
		return employee

class Company:
	def __init__(self):
		self.employees = []

	def add_employee(self, name, id, salary):
		self.employees.append({'name': name, 'id': id, 'salary': salary})

	def __iter__(self):
		return EmployeeIteration(self.employees)

company = Company()
company.add_employee('John', 1, 1000)
company.add_employee('Jane', 2, 2000)
company.add_employee('Boob', 3, 3000)
company.add_employee('Door', 4, 4000)

for employee in company:
	print(employee['name'])
	print(employee)

print("-----------------")

def my_genFunc():
    yield 1
    yield 2
    yield 3

gen = my_genFunc()
print(next(gen))
print(next(gen))
print(next(gen))

print("-----------------")

