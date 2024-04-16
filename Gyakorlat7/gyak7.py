# OOP 1
# Osztály, példány, statikus és osztálymetódusok, öröklődés,
# többszörös öröklődés

class Person:

    __slots__ = ('name', 'personal_id')

    species = 'Homo sapiens' # statikus változó


    def __init__(self, name, personal_id):
        self.name = name
        self.personal_id = personal_id

    @staticmethod
    def print_species_static():
        print(Person.species)

    @classmethod
    def print_species_class(cls):
        print(cls.species)

    # Osztálymetódusok: alternatív konstruktorként is használhatók

    @classmethod
    def from_json(cls, input_str):
        splitted_str = input_str.split(',')
        name = splitted_str[0]
        id = splitted_str[1]
        return cls(name, id)


p1 = Person("Jack", 123)
print(p1.name)

p2 = object.__new__(Person) # itt jön létre az objektum
p2.__init__("Teszt Elek", 456)
print(p2.name)

# p2.x = 15
# print(p2.x)

# Példányosítás az alternatív konstruktorral:
p3 = Person.from_json("Gipsz Jakab, 789")
print(p3.name)


# Statikus és osztálymetódusok
# @classmethod - dekorátor

class MyClass:

    def instance_hello(self): # példánymetódus
        print(f"Hello példány: {self}!")

    @classmethod
    def class_hello(cls):
        print(f"Hello osztály: {cls}")


    @staticmethod
    def say_hello():
        print("Hello static!")

newclass = MyClass()
newclass.instance_hello()
newclass.class_hello() # az osztályon keresztül történik az átadás
newclass.say_hello()

MyClass.class_hello()
MyClass.say_hello()

# Öröklődés

class User(Person):

    species = 'Homo informaticus'

    def __init__(self, name, personal_id, login_name):
        super().__init__(name, personal_id) # super() = Parent.__init__(self)
        self.login_name = login_name

u1 = User("Lutz Gizella", 569, 'user458')
print(u1.species)

# Öröklődés és statikus metódusok
Person.print_species_static()
Person.print_species_class()

User.print_species_static()
User.print_species_class()

print(type(u1))
print(isinstance(u1, User))
print(isinstance(u1, Person))

# Többszörös öröklődés

class Student:

    def __init__(self, student_id):
        self.student_id = student_id


class NeptunUser(User, Student):
    def __init__(self, name, personal_id, login_name, student_id, neptun_code):
        User.__init__(self, name, personal_id, login_name)
        Student.__init__(self, student_id)
        self.neptun_code = neptun_code

neptun_user = NeptunUser("Hold Viola", 123, 'viola99', 5698, 'AFG58t')


# Method resolution order
# Diamond MRO:
# 1: saját metódus/field --> 2: első ősosztály metódus/field
# --> második ősosztály metódus/ field --> ős-ősosztály metódus/field
#
#       A
#    /     \
#   B       C
#    \     /
#       D

class A:
    num = 10

class B(A):
    #num = 20
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.num)
print(D.mro())

#---------------------------------------------------------------
# Challenge 3:
#-------------
# Hozzunk létre egy osztályt, ami a PÉLDÁNYOSÍTÁSKOR visszaad egy
# n x n-es mátrixot (n legyen az osztály attribútuma), feltöltve
# 0, 1 és 2 értékekkel random.

# Az NEM JÓ megoldás, ha írunk egy metódust az osztályba, ami
# legenerálja a mátrixot!

# A feladatot több szinten is meg lehet oldani,
# ha úgy írjuk meg az osztályt, hogy a belőle származó példány
# önmaga egy iterálható, kétdimenziós adatszerkezet, az plusz egy
# pontot ér, tehát 2 challenge megoldásával ér fel a feladat.