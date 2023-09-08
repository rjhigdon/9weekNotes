##########Comparison Operators##########

#All the comparison operators ( ==, !=, >, <, >=, <= ) Are the same in Python as in Js.
#We can combine/chain these operators like so: 
1<2<3 #returns True
1>2<3 #returns false
1<2 and 2<3 #returns true
"h" == "h" and 2==2 #returns true
#"and" needs both or all statments to be true to return true 
#"or" only needs one to be true
#"not" requires the opposite of the statement to be true. FOr example:
1==1 #returns true
not 1==1 #returns false


########## lists, tuples, and sets ##########

#LISTS are mutable and ordered list of items with brackets:
my_list=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
# #these are good forwhen you need to store an ordered collection 
# # of items that may change over time, such as a list of numbers, names, or any other data.
# #common methods for lists include:
    my_list.append(item)
    my_list.insert(index, item)
    my_list.remove(item)    #removes first occurence of item
    my_list.pop(index)
    my_list.count(item)     #counts occurence of an item
    my_list.sort()
    my_list.reverse()
    my_list.clear()
    
# #TUPLES are immutable, which means you cannot modify their elements after creation. 
# # Once defined, a tuple's elements cannot be changed. declare them like this:
my_tuple=(1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8)
# #These are useful when you want to store a collection of items that should not be modified, 
# # such as coordinates, database records, or function return values.
# #Common methods are different because tuples are immutable but here:
    count = my_tuple.count(item)    #counts occurence of item in tuple
    element = my_tuple[index]       #Accesses item by index
    subset = my_tuple[start:end]    #Accesses series of items by index
    new_tuple = tuple1 + tuple2     #Concatenates tuples
    repeated_tuple = my_tuple * n   #repeat tuples
    

# #SETS are not only unordered but unique, meaning they delete duplicate values
my_set={1,2,3,4,5,6,7,8}
# #common methods for sets are as follows:
    my_set.add(item)
    my_set.remove(item)
    my_set.discard(item)    #Remove an Item Safely (No Error if Item Not Present)
    my_set.clear()
    
# Lists and tuples allow indexing and slicing (accessing elements by position), while sets do not support this because they are unordered.
# Lists and tuples can contain elements of different data types, whereas sets are typically used for homogeneous collections.
# Lists and tuples use square brackets and parentheses for indexing, respectively, while sets use curly braces (or the set() constructor).
# Lists and tuples are iterable, allowing you to loop through their elements, while sets are also iterable, but their order is not guaranteed.


########## if, elif, else Statements ##########

#if is your basic conditional: if something happens, do some thing
#elif give instructions to when something else happens(else if => elif)
#else gives instructions to when none of those things happens

location = "Bank"

if location == "Auto Shop":
    print ("cars are cool")
elif location == "Store":
    print("Food is Cool")
elif location == "Bank":
    print ("Money is Cool")
else:
    print("I don't know what's Cool")
    
########## for loops ##########

#allows us to iterate over an object
#the most basic syntax for this is as follows:

mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum =0 

for num in mylist:
    print(num)
    
#num just represents the iterable items in that list
for num in mylist:
    print("this item in the iterable is a number")

for num in mylist:
    if (num%2 == 0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        
for num in mylist:
    list_sum = list_sum + num
    
    print(list_sum) #prints result after every iteration
print(list_sum)     #prints only the final result
 
#you dont even have to declare a variable for it to iterate. You can just slap something in there:

for letter in "Hello World":
    print(letter)
    
########## range() function ##########

#used in for loops and it takes in start, stop, and step parameters. 
#this is the tool for editing iteration specifics. 
# Instead of (i=0; i<arr.length; i++) like in JS, we can do:
for num in range(1,6,1):
    print(num)
#this prints 12345 (starts at 1, counts to 6 but doesnt count 6, by 1)

for num in range(2,10,2):
    print(num)
#this prints 2468 (starts at 2, counts to 10 but doesnt count 10, by 2)

#if we wanna cast it to a list we can do it like this:
range_list = list(range(2,10,2))
print(range_list)

########## Enumerate ##########

index_count = 0

for letter in "abcdefgh":
    print(f"the letter {letter} is at index {index_count}")
    index_count += 1
#prints: "the letter a is at index 0" etc
#this shows how frustrating indexing strings like this for for loops can be
#instead of this we will enumerate this like so:

word = "abcdefgh"

for letter in enumerate(word):
    print(letter)
#prints tuples of the letter and index(0, 'a') /n (1, 'b') /n (2, 'c')
#you can also enumerate separatelyn like so: 
word = "abcdefgh"

for index, letter in enumerate(word):
    print(index)
    print(letter)
#prints items on each like like: "0\na\n1\nb" etc

########## zip() ##########

#this is a for loop operator like enumerate and will 
#zip together lists into tuples at matching positions like so:

mylist1 = [1, 2, 3]
mylist2 = ['a','b','c']
mylist3 = [124, 146, 543]
for item in zip(mylist1,mylist2,mylist3):
    print(item)
#--> (1, a, 124)\n(2,b,146)\n(3,c,543)
resultlist = list(zip(mylist1,mylist2,mylist3))
print(resultlist)
#--> [(1, 'a', 124), (2, 'b', 146), (3, 'c', 543)]

########## in operator ##########

#simply checks lists for items
"a" in mylist1
#--> False
"a" in  mylist2
#-->True
"a" in "apple"
#--> True

#it works in dictionaries too
d= {'mykey':345}
345 in d.values()
#--> True

########## min, max, and random ##########

#reminder: mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] declared in ln. 73
min(mylist)
#--> 1
max(mylist)
#--> 10

#for random, there is a built in random library for python:
from random import shuffle  #this is importing the shiffle module for the random library
shuffle(mylist)
print(mylist)
#-->[5, 4, 7, 10, 8, 9, 3, 6, 1, 2] or some other randomization of mylist'
#this isnt returning anything btw. It is operating "in place"
#this random library has so many other modules as well like so:
from random import randint #ranndint = random integer
randint(0,100)
#--> 91 or some other random integer between 0 and 100
#you can also assign the random into to a variable
radnom_number = randint(0,100)

########## User input ##########

#run ln 245, type in input, then run 246
result = input("What is your favorite number?")
print(result)
#the result of this will always be a string unless we specify it otherwise like so 
int(result)
float(result)

########## List comprehension ##########

mystring = "hello"
mystrlist = []

for letter in mystring:
    mystrlist.append(letter)
print(mystrlist)
#--> ['h', 'e', 'l', 'l', 'o']
#this is the lame multiline way of creating a list
#Instead of that you shoudl do:

mystring = "hello"
mystrlist = [letter for letter in mystring]
print(mystrlist)
#--> ['h', 'e', 'l', 'l', 'o']

#you can also do this to perform functions as it is iterating into a new list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
mysqrlist = [num**2 for num in mylist] # or mysqrlist = [num**2 for num in range(0,10)]
print(mysqrlist)
#--> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# you could do a unit converter like this
miles = [1, 2, 2.5, 5, 8.1]
feet = [num*5280 for num in miles]
print(feet)
#-->[5280, 10560, 13200.0, 26400, 42768.0]

########## and elif in list  ########## 

results = ["even" if num%2==0 else "odd" for num in range(0,10)]
print(results)
#-->['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

########## Nested for loops  ########## 

mynestedlist = []

for x in [2,4,6]:
    for y in [1,3,5]:
        mynestedlist.append(x+y)
print(mynestedlist)
#-->[3, 5, 7, 5, 7, 9, 7, 9, 11]
#similarly as in lsit comprehension we can one line this one:

mynestedlist = [x+y for x in [2,4,6] for y in [1,3,5]]
print(mynestedlist)
#-->[3, 5, 7, 5, 7, 9, 7, 9, 11]


########## classes ##########

class Dog(): #classes have camel casing
    def __init__(self,breed):   #__init__ method is the class constructor. self keyword indicates the instance of the class
        self.breed = breed      #this assigns attribute name to the class parameter
#this creates the class
my_dog = Dog(breed = "CKCS")
type(my_dog)

#another example:
from random import randint
class Dog():
    def __init__(self, name, breed, age, color, alive):
        self.name = name 
        self.breed = breed
        self.age = age
        self.age = color 
        self.alive = alive
        
    def bark(self, num):     #this allows us to use methods in classes 
        print(f"BARK! My name is {self.name} and I am {self.age} years old, and the random number I chose this time is {num}")
        
my_dog = Dog("Arlo", "CKCS", "multi", 8, True)
my_dog.bark(randint(0,100))           #this calls the method we created
Lukes_dog = Dog("Bolt", "psycho", "brown", 5, True)

#final example:

class Circle:
    pi = 3.14159265
    
    def __init__(self, radius=1):
        self.radius= radius
    def get_circum(self):
        return self.radius * self.pi * 2

my_circle = Circle(20)
my_circle.get_circum()

########## Inheritance ##########

class Animal:
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

class Dog(Animal):      #class Dog has now inherited everything from the Animal class. 
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):         #we can edit the who_am_i method by simply restating that here.... 
        print("I am a dog")     #but we can simply leave it and it could be reused 1 to 1
my_dog = Dog()
my_dog.eat()        #prints the old methid from animals
my_dog.who_am_i()   #prints the new methid from Dogs because we overwrote in ln 355

########## Polymorphism ##########

class Dog():
    def __init__(self, name):
        self.name = name 
       
    def speak(self):    
        return(self.name + " says woof!")

class Cat():
    def __init__(self, name):
        self.name = name 
       
    def speak(self):    
        return(self.name + " says meow!")
        
arlo = Dog("Arlo")  
merlin = Cat("Merlin")  
print(arlo.speak())
print(merlin.speak())

for pet in [arlo, merlin]:
    print(type(pet))        #this is telling us what each item in the list is 
    print(pet.speak())      #this is telling us what happens when each has their speak method called
    
#a better way to handle this operation is to make a head class

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self): 
        raise NotImplementedError("Subclass must implement this method") 
    #this is only a placeholder/ header class. We dont actually want/need to use them
    
########## Dunder Methods ##########

def __init__(self, ...): #Constructor method. Initializes a new object when it's created.
def __str__(self): #Defines the string representation of an object when str() or print() is called on it.
def __repr__(self): #Defines the "official" string representation of an object, typically used for debugging.
def __len__(self): #Defines the behavior of len() when called on an object of the class.
def __getitem__(self, key): #Allows objects of the class to be indexed using square brackets.
def __setitem__(self, key, value): #Allows objects of the class to be assigned values using square brackets.
def __delitem__(self, key): #Defines behavior for deleting items using del and square brackets.
def __iter__(self): #Defines how objects of the class should be iterated over using a loop.
def __next__(self): #Specifies what happens when the next() function is called on an iterator.
def __contains__(self, item): #Controls the behavior of the in operator for objects of the class.
def __eq__(self, other): #Defines the behavior of the equality operator ==.
def __ne__(self, other): #Defines the behavior of the inequality operator !=.
def __lt__(self, other): #Defines the behavior of the less-than operator <.
def __le__(self, other): #Defines the behavior of the less-than-or-equal-to operator <=.
def __gt__(self, other): #Defines the behavior of the greater-than operator >.
def __ge__(self, other): #Defines the behavior of the greater-than-or-equal-to operator >=.
def __add__(self, other): #Defines behavior for the + operator.
def __sub__(self, other): #Defines behavior for the - operator.
def __mul__(self, other): #Defines behavior for the * operator.
def __truediv__(self, other): #Defines behavior for the / operator (in Python 3).
def __floordiv__(self, other): #Defines behavior for the // operator (floor division).
def __mod__(self, other): #Defines behavior for the % (modulo) operator.
def __pow__(self, other, modulo=None): #Defines behavior for the ** (exponentiation) operator.
def __contains__(self, item): #Defines the behavior of the in operator.
    
##########.txt File Basics##########
# After making your txt file you can open, write, and read it using the code:
myfile = open("myfile.txt")   #Opens the desired file
myfile.write("hello text")    #Writes to it
myfile.read()                 #Reads it with /n for lines breaks
myfile.readlines()            #This reads line by line as different objects we can do:
myfile.close()                #Closes it ()

# #An important note about reading is that you have to reset the cursor to read it multiple times.
# #To do this you must use this code:
myfile.seek(0)

# #You are able to access .txt's in other folders easily by assigning the file a variable name by path. For example:
distantfile = open("C:\\users\\etc\\etc\\etc\\")

# #In order to avoid errors and such we must close the txt before we can delete it or other things. There is a way to get around the opening and closing:
with open("myfile.txt") as myfile:
    contents = myfile.read()
# #Now we can access myfile as contects without having to worry about opening and closing it

# #Setting a mode for the files allows for setting of permissions so things don't happen to it that you don't intend.
# #The different modes avaialable are as follows: 
# w = write
# r = read
# a = append
# r+ = read and write
# w+ = overwriting, reading, and making new files
# default mode = "r"

with open("myfile.txt", mode="r") as myfile:
#         print(myfile.read())    #this returns the contents because r = read

with open("myfile.txt", mode="w") as myfile:
#         print(myfile.read())    #this returns an error because w = write
        
with open("myfile.txt", mode="a") as myfile:
#     myfile.write("Some more text")   #this appends "some text" to the end of the already written text. 
#                                 #mode a places the cursor at the end of the text just like seek(0) places it at the beginning
                                    
with open("myfile.txt", mode="w") as myfile:
#     myfile.write("just a text")   #this overwrites the contents of myfile to "just a text"