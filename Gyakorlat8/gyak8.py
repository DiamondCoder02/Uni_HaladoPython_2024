# Attribútum, tulajdonság (property), deszkriptor

class Program:
    language = 'Python'
    version = '3.11'

print(Program.__dict__)

print(Program.language)
print(getattr(Program, 'version'))
print(getattr(Program, 'x', 'N/A'))

Program.x = 100
print(getattr(Program, 'x'))

delattr(Program, 'x')
print(Program.__dict__)

# Hívható osztály attribútumok

class NewProgram:
    language = 'Python'

    @staticmethod
    def say_hello():
        print(f"Hello from {NewProgram.language}!")

    def __init__(self, version):
        self.version = version

print(NewProgram.__dict__)
NewProgram.say_hello()

print(getattr(NewProgram, 'say_hello'))
print(NewProgram.say_hello)

new_progi = NewProgram(3.12)
print(new_progi.__dict__)

print(type(new_progi))
print(new_progi.__class__)

class Person:

    def __init__(self, name):
        self.name = name


p = Person('Gizi')
print(hex(id(p)))
print(type(p))
print(p.__dict__)
print(Person.__dict__)

# Attribútum létrehozása futási időben

# Módszer 1:
def say_hi(self):
    return f"{self.name} says hi!"

# Módszer 2:
from types import MethodType

p3 = Person("Béla")
p3.say_hello = MethodType(lambda self: f"Hello {self.name}!", p3)
print(p3.say_hello())

# Tulajdonság - property

class MyClass:
    def __init__(self, language):
        self._language =language

    def get_language(self):
        print("language getter called...")
        return self._language

    def set_language(self, value):
        print("language setter called...")
        self._language = value

    language = property(fget=get_language, fset=set_language)


mc = MyClass('Python')
mc._language = 'Java'
print(mc._language)
print(mc.get_language())
mc._language = 'C++'
mc.set_language('C#')

mc.language = 'Python'

class Student:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("name getter called...")
        return self._name

    def set_name(self, value):
        print("name setter called...")
        # Név ne lehessen üres sztring vagy szám
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError('A név nem lehet üres sztring vagy szám.')

    def del_name(self):
        del self._name

    name = property(fget=get_name, fset=set_name, fdel=del_name)

s = Student('Alex')
print(s.__dict__)
print(s.name)

s.name = 'Peter'
print(s.name)

del s.name
print(s.__dict__)

# property --> dekorátor

class MyValue:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print("x getter called")
        return self._x

    @x.setter
    def x(self, value):
        print("x setter called")
        self._x = value

    @x.deleter
    def x(self):
        print("x deleter called")
        del self._x

mv = MyValue(25)
print(mv.x)
mv.x = 30
del mv.x

# Computed property

import math

class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return math.pi * self.r**2

c = Circle(1)
print(c.area)
c.r = 2
print(c.area)

# Deszkriptorok

# deszkriptor protokol: __get__, __set__, __delete__
# 2 típus: data deszkriptor: mindhárom metódus implementálva van
#        : non-data deszkriptor: csak a __get__ metódus van implementálva

class Point2DWithGetterSetter:
    def __init__(self):
        self._x = None
        self._y = None

    def get_x(self):
        print("Getting x")
        return self._x

    def set_x(self, value):
        print("Setting x")
        self._x = value

    def get_y(self):
        print("Getting y")
        return self._y

    def set_y(self, value):
        print("Setting y")
        self._y = value

    x = property(get_x, set_x)
    y = property(get_y, set_y)

obj1 = Point2DWithGetterSetter()
obj1.x = 10
obj1.y = 20
print(obj1.x)
print(obj1.y)

# Ugyanez deszkriptorral:
class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Desc: getting {self.name}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Desc: setting {self.name}")
        instance.__dict__[self.name] = value

class Point2DWithDescriptor:
    x = Descriptor('x')
    y = Descriptor('y')

obj2 = Point2DWithDescriptor()
obj2.x = 30
obj2.y = 50
print(obj2.x)
print(obj2.y)

#------------------------
# Challenge 4:

# Írjon egy osztályt ami egy attribútummal rendelkezik, az attribútumnak
# adjunk egy kezdeti értéket.
# Deszkriptor (osztály) segítségével valósítsuk meg azt, hogy az
# attribútum értéke csak akkor legyen módosítható, ha a megadott érték
# nagyobb, mint az addigi érték.
# Kommentek!!!
