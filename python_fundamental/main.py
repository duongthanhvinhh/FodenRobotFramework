name = "Foden"
full_name = "Foden Duong"
print(name in full_name) #substring check -> return true or false
age = 26
#print(name + age) TypeError: can only concatenate str (not "int") to str
print("{} {}".format(name, age))
name_with_spaces = " Foden   "
print(name_with_spaces.strip()) #Return a copy of the string with leading and trailing whitespace removed.
print(name_with_spaces.lstrip()) #Remove spaces in left
print(name_with_spaces.rstrip()) #Remove spaces in right

# List - Example code
values = [1, 2, "Foden", 78]
print(values[0])
print(values[-1])
print(values[1:3])
values.insert(3, "Duong")
print(values)
values.append("End")
print(values)
values[2] = "Vinh"
print(values)
del values[0]
print(values)

# Tuple - Example code
tuple_example = (1, 2, "Foden", 78)
print(tuple_example[1])
# tuple_example[1] = 3 -> TypeError: 'tuple' object does not support item assignment

# Dictionary - Example code
dictionary_example = {1:"Foden", 2:"Duong", "Vinh":26}
print(dictionary_example[2])
print(dictionary_example["Vinh"])

dic = {}
dic["Name"] = "Foden"
dic["Age"] = 26
print(dic) #Output: {'Name': 'Foden', 'Age': 26}

#Data types in Python
    #1: Numeric
            # int
            # float: accurate upto 15 decimal places
            # complex: like 100 + 3j
    #2: String
    #3: List
            # List is a data types that allows multiple values with different data types
            # values = [1, 2, "Foden", 78]
            # print(values[0])
            # print(values[-1]) -> Output: 78, minus one refer to the last element in the list
            # print(values[1:3]) -> Output: [2, 'Foden'], returns sub list from indices 1 to 2
            # values.insert(3, "Duong") -> [1, 2, 'Foden', 'Duong', 78]
            # values.append("End") -> [1, 2, 'Foden', 'Duong', 78, 'End']
            # values[2] = "Vinh" -> [1, 2, 'Vinh', 'Duong', 78, 'End']
            # del values[0] -> [2, 'Vinh', 'Duong', 78, 'End']
    #4: Tuple
            # Does the same thing as List, but List is mutable, and Tuple is immutable
            # Means after declare a tuple, you cannot update it
    #5: Dictionary
            # Is unordered sequence of data of key-value pair form
            # dictionary_example = {1:"Foden", 2:"Duong", "Vinh":26}

# Flow-control

#1 If-else condition
name = "Foden Automation"
if name.__contains__("Automation"):
    print(name + " is an automation tester.")
    print("His fullname is: Foden Duong")
else:
    print(name + " is a Scrum master")

#2 For loop
numbers = [1, 2, 4, 5, 7]
for number in numbers:
    print(number*2)

sum_first_five_numeric_numbers = 0
for i in range(1, 6):
    sum_first_five_numeric_numbers += i
print(sum_first_five_numeric_numbers)

odd_numbers = []
for j in range(1, 10, 2): # 2 means will jump 2, step = 2
    odd_numbers.append(j)
print(odd_numbers) #Output: [1, 3, 5, 7, 9]

first_ten_numbers = []
for k in range(10):
    first_ten_numbers.append(k)
print(first_ten_numbers) #Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#3 While loop
wl = 5
while wl > 1: # we can use continue/break the same as in Java
    if wl != 3:
        print(wl)
    wl = wl - 1


# Function
def greet_candidate(candidate_name):
    print("Welcome " + candidate_name)

greet_candidate("Foden")

def add_two_integers(num1, num2):
    return num1 + num2

print(add_two_integers(2, 4))


# OOP concepts
class Calculator:
    # Default constructor
    # def __init__(self):
    #     print("I am called automatically when object is created")

    # Constructor with argument: In python we can not define multiple constructor for a class, so if we want to create an obj with default constructor,
    # in the constructor with argument, we may need to add the default value for the argument
    def __init__(self, my_name="Unknown", my_age=0):
        print("I am called automatically when object is created")
        self.name = my_name
        self.age = my_age

    num = 100 # this one is class variable
    def get_new_num_value(self):
        return self.num + 1

    def get_info_user(self):
        return "{} : {} years old.".format(self.name, self.age)
calculator_default = Calculator() #Syntax to create new object of Calculator class , here the default constructor is called automatically
print(calculator_default.num)
print(calculator_default.get_new_num_value())
print(calculator_default.get_info_user()) #Output: Unknown : 0 years old.

calculator_with_arg = Calculator("Foden", 26)
print(calculator_with_arg.get_info_user()) #Output: Foden : 26 years old.


# Example full OOP Python
from abc import ABC, abstractmethod #abc here is the name of python file -> abc.py
class Animal(ABC): # Abstraction + Inheritance base
    def __init__(self, unique_name):# Encapsulation
        self._name = unique_name # Encapsulation because the _name is intended to be private in Python

    @abstractmethod
    def speak(self): # Abstraction: Only show what is needed, do not show the details
        pass

class Dog(Animal): # Inheritance
    def speak(self): # Polymorphism - implement the speak() method follow the behaviour of Dog (Note: Python does not support overloading, only overriding)
        return f"{self._name} says Woof!"
class Cat(Animal): # Inheritance
    def speak(self): # Polymorphism - implement the speak() method follow the behaviour of Dog
        return  f"{self._name} says Meow!"
dog = Dog("Buddy")
cat = Cat("Moon")
print(dog.speak()) #Output: Buddy says Woof!
print(cat.speak()) #Output: Moon says Meow!


#Must call parent constructor explicitly if the parent's constructor is not a default constructor
class Parent:
    def __init__(self, name_parent):
        print(f"Parent constructor called. Name: {name_parent}")

class Child(Parent):
    def __init__(self, name_child, age_child):
        # ✅ Must call parent constructor
        super().__init__(name_child)
        print(f"Child constructor called. Age: {age_child}")

child = Child("Alice", 25)


#In case the parent class constructor takes more arguments than the child
class Parent1:
    def __init__(self, name_parent1, age_parent1, country):
        print(f"Parent: name={name_parent1}, age={age_parent1}, country={country}")
        self.name_parent1 = name_parent1
        self.age_parent1 = age_parent1
        self.country = country

class Child1(Parent1):
    def __init__(self, name_child1, age_child1):
        # ✅ You must call the parent constructor with all required arguments
        # You can hardcode or compute the remaining one(s)
        super().__init__(name, age, country="USA")
        print(f"Child: name={name_child1}, age={age_child1}")

child1 = Child1("Alice", 30)

#Or can use **kwargs
    # class Parent:
    #     def __init__(self, name, age, country):
    #         print(f"Parent: name={name}, age={age}, country={country}")
    #
    # class Child(Parent):
    #     def __init__(self, name, age, **kwargs):
    #         super().__init__(name, age, **kwargs)
    #
    # child = Child("Bob", 25, country="Canada")

