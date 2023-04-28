#
# Copyright Zach Stone 2023
#
# BSD Licns
#

import sys
#print (sys.argv[1])
#print (sys.argv[2])

opt = sys.argv[1]
person = sys.argv[2]

        
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
    

