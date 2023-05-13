#
# Copyright Zach Stone 2023
#
# BSD License
#
#
# Usage: python3 basic_structures.py (-h|-g) (name)




import sys
import math
import numpy as np 
from makeblock import MegaPi,SerialPort


#print (sys.argv[1])
#print (sys.argv[2])

opt = sys.argv[1]
person = sys.argv[2]


# If Or Input Check
if (len(sys.argv) < 3) or (len(sys.argv) > 3):
    print("usage: python3 basic_structures.py [-h|-g] [name]")
    quit() 


# Greeting Function
def greeting(greetingType):
     i = 0
     while i < 12:
         i = i + 1
         print(greetingType + ", " + person + "! (" +str(i) + ")")


# Main Code
if opt == '-h':
     greeting('Hello')
elif opt == '-g':
     greeting('Goodbye')


# Fruit
fruits = ("apple", "banana", "cherry")
for index, fruit in enumerate(fruits):
    print((index + 1), fruit)


# Mathematical Functions
print("Math Time")
theNumber = 8.2394290
print(math.ceil(theNumber))
print(math.pi)

# Standard deviation example
a = np.array([1, 2, 3, 4])
print(np.std(a))
