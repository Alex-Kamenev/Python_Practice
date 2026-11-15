#Import random to use later for testing function
import random

#Main function
#Takes alist as input, checks if the list has duplictes and returns True/False
def hasDuplicates(values):
  """Return whether an iterable of hashable values contains equal items."""
  seen = set()
  for value in values:
    if value in seen:
      return True
    seen.add(value)
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
if __name__ == '__main__':
  testDup()
