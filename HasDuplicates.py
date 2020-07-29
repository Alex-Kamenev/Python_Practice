#Import random to use later for testing function
import random

#Main function
#Takes alist as input, checks if the list has duplictes and returns True/False
def hasDuplicates(list):
  #make new dictionary
  myMap = {}

  #populate the dictionary by iterating over the list 
  #prior to inserting in dictionary check if entry with set value already exists if so returen True
  for i, value in enumerate(list):
    key = value.__hash__()
    if value == myMap.get(key):
      return True
    else:
      myMap[key] = value
  return False

#Healper function to generate random list
def randomList():
  l = []
  for i in range(5):
    l.append(random.randrange(100))
  print(l)
  return l

#Testing method
def testDup():
  for i in range(10):
    l_i = randomList()
    print(hasDuplicates(l_i))

#call testing method
testDup()
