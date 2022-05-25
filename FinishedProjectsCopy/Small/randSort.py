import random as rand
import math as math
import copy as copy #why the hell do i need to import a module for this or am
                    #i just dumb

def randomList(size):
  array =  [rand.randint(0,10) for i in range(size)]
  return array

# function adapted to python from: 
# https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
def shakeList(array):
  currentIndex = len(array)
  # While there remain elements to shuffle...
  while (0 != currentIndex):
    # Pick a remaining element...
    randomIndex = int(math.floor(rand.random() * currentIndex))
    currentIndex -= 1
    # And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]]

  return array

if __name__ == "__main__":
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('--side', '-s', dest="phrase", required=False, \
 action='store', default="left right", help='Which side starts on?')
  parser.add_argument('--time', '-t', dest="duration", required=False,
 default=10, action='store', help='How many blinks ya want?')
  args = parser.parse_args()

  myarray = randomList(5)

  sortedCopy = copy.copy(myarray) #copy is a library, copy is also a function of
                                #copy is also a function of the copy library

  sortedCopy.sort()
  print("original array: {}".format(myarray))
  print("sorted array: {}".format(sortedCopy))
  i = 0
  while (i < 20):
    if (myarray == sortedCopy): 
      print("yay")
      break
    shakeList(myarray)
    print("randomly shuffled: {}".format(myarray))
    i += 1
  print("it took this many shuffles: {}".format(i))

  #blink(args.phrase, args.duration)
