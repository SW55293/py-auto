import sys
import os 

a = sys.argv[1]

if a == "1":
    print('a is ', a)
else: 
    print('not 1 instead a is', a)

#this program captures the users input when passed along 
#with the python run code and prints out the right block
#ex: python3 import-2.py 1
#it needs a number or just any value to determine if the if block applies
