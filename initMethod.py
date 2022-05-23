"""The __init__ method is similar to constructors in C++ and Java.
Constructors are used to initializing the object’s state.
Like methods, a constructor also contains a collection of
statements(i.e. instructions) that are executed at the time of Object creation.
It runs as soon as an object of a class is instantiated. 
The method is useful to do any initialization you want to do with your object.
"""

class Person:
    def __init__(self, name):
        self.name = name
        
    def prints(self):
        print("Hello I am ", self.name)
        
p1 = Person("Jack")

p1.prints()