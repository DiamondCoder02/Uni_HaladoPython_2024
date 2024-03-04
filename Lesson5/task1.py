# Closures, decorators

# Scopes: global, local

def outer2():
    x = 'Java'
    def inner2():
        global x
        x = 'Python'
    inner2()
    print(x)
outer2()

def outer():
    x = 'Java' # free variable
    def inner(): # closure
        nonlocal x
        x = 'Python'
    inner()
    print(x)
outer()

print('------------------------')

def outside(x):
	def inside(y):
		return x + y
	return inside

temp_func = outside(10)
sum = temp_func(5)
print(sum)

print('------------------------')

def counter():
	count = 0 # free variable
	def incl1():
		nonlocal count
		count += 1
		return count
	def incl2():
		nonlocal count
		count += 1
		return count
	return incl1, incl2
inc1, inc2 = counter()
print(inc1())
print(inc2())
print(inc1.__code__.co_freevars)
print(inc2.__code__.co_freevars)
print(inc1.__closure__)
print(inc2.__closure__)

print('------------------------')

# Decorators

def counter_func(fn):
	count = 0
	def inner(*args, **kwargs):
		nonlocal count
		count += 1
		print(f'Function {fn.__name__} was called {count} times')
		return fn(*args, **kwargs)
	return inner

def add3(a, b=0):
	return a + b

add2 = counter_func(add3)

result = add2(10, 20)
result = add2(10, 20)
result = add2(10, 20)
result = add2(10, 20)
print(result)

print('------------------------')

# Decorators:
# 1. Function accepts another function as parameter
# 2. It returns a closure
# 3. The inner function accepts any combination of parameters
# 4. The inner function calls the original function

@counter_func
def add(a, b=0):
	return a + b

# Def: my_func = decorator(my_func) --> @decorator

from functools import reduce, wraps
from time import perf_counter

def timer(fn):
	def inner(*args, **kwargs):
		start = perf_counter()
		result = fn(*args, **kwargs)
		end = perf_counter()
		elapsed = end - start
		print(f'Function {fn.__name__} took {elapsed} seconds')
		return result
	return inner

# Fibonacci 
# 1. For clycle // 2. Recursion // 3. reduce()

def fib_recursion(n):
	return n if n <= 1 else fib_recursion(n-1) + fib_recursion(n-2)

@timer
def fib_rec(n):
    return fib_recursion(n)

@timer
def fib_loop(n):
    fib_0 = 0
    fib_1 = 1
    for i in range(2, n+1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

@timer
def fib_reduce(n):
    initialValues = [0, 1]
    fib_func = lambda fib, _: (fib[1], fib[0] + fib[1])
    fib_number = reduce(fib_func, range(n), initialValues)
    return fib_number[0]

print(fib_rec(10))
print(fib_loop(20))
print(fib_reduce(20))

print('------------------------')

# @wraps

def my_decorator(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(f'Calling function {func.__name__}')
		result = func(*args, **kwargs)
		print(f'Function {func.__name__} returned {result}')
		return result
	return wrapper

@my_decorator
def example_function():
	"""
	Example function
	:return: None
	"""
	print('Called example function')

example_function()
print('---')
print(example_function.__name__)
print(example_function.__doc__)

print('------------------------')
