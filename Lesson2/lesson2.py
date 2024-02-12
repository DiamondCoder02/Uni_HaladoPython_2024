# References and unpacking

myVar = 987
print(id(myVar))
otherVar = myVar
print(id(otherVar)) # shared reference

import sys
print(sys.getrefcount(myVar)) # 5 references

del otherVar
print(sys.getrefcount(myVar)) # 4 references

myVar += 50
print(myVar)
print(id(myVar))

print('------------')

myList = [1,2,3,4]
print(myList)
print(id(myList))
myList.append(12)
print(myList)
print(id(myList))

print('------------')

myTuple = (['a', 'b'],['d', 'e'])
print(myTuple)
print(id(myTuple))
myTuple[0].append('f')
print(myTuple)
print(id(myTuple))

print('------------')
num1 = 999
num2 = 999
print(id(num1))
print(id(num2))

list1 = [1,2,3]
list2 = [1,2,3]
print(id(list1))
print(id(list2))

print('------------')

# Strong, weak, circular references

class Circulation:
    def __init__(self):
        self.obj = None

obj1 = Circulation()
obj2 = Circulation()

# obj1.obj = obj2
# obj2.obj = obj1

import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

obj3 = MyClass("I have a weak reference")
weak_ref = weakref.ref(obj3)
if weak_ref() is not None:
    print("The object is alive")
else:
    print("The object is deleted")

# del obj3

print('------------')

# Arguement VS Parameter
def add(x, y=2):
    return x+y

print(add(4,5))
print(add(y=5, x=4))
print(add(6))

print('------------')

# Unpacking

whatAmI = 9,8,7
print(type(whatAmI))

a,b,c = 1,2,3
print(c)
print(type(b))

x,y,z = [7,8,9]
print(y)

a2 = 10
b2 = 20
temp = a2
a2 = b2
b2 = temp
print(a2, b2)

a3 = 30
b3 = 50
print(a3, b3)
a3, b3 = b3, a3
print(a3, b3)

print('------------')

s1, s2, s3 = 'XYZ'
print(s2)

s = {'h', 'i'}
c1, c2 = s
print(c1, c2)

myDict = {'key1':1, 'key2':2, 'key3':3}
k1, k2, k3 = myDict.items()
print(k1, k2, k3)

l1,l2,*l3,l4 = [1,2,3,4,5,6,7,8,9]
print(l3)
print(l1,l2,l4)

print('------------')

myList1 = [1,2,3]
myList2 = [4,5,6]
listSum = [myList1, myList2] # 2D list
print(listSum)
listSum = [*myList1, *myList2] # 1D list
print(listSum)

# Nested unpacking

z1, z2, *z3, (x1,x2,x3) = [1,2,3,4,5,'XYZ']
print(z1, z2)
print(z3)
print(x1, x2, x3)

# Task1: 
# Write a function that can accept any parameter, in any format and calculates the average
def avr(*nums):
    return round(sum(nums) / len(nums), 2)
print(avr(60,50,30))

numList = [6,99,785,25,-9,-7,81]
print(avr(*numList))

studentDict = {"asd":4, 'khs':5, 'yvcv':4}
print(avr(*studentDict.values()))

# Task2:

numList1 = [5,-9,-8,87,63]
numList2 = [45,126,9876,-87,12]
numList3 = [1,0,-5,3]

sumList = [*numList1, *numList2, *numList3]
print(sumList)

minValue, *middleValue, maxValue = sorted(sumList)
print(minValue, maxValue)