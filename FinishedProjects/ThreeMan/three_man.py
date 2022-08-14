from random import randint
from time import sleep
import numpy as np
import argparse

# note that this version of threeman is different from what you'll find via google
# https://eus.wiki/3_Man (top result)
# this version of threeman I learned in Manhattan, Kansas, in 2020
#
# the goal of this program is to determine if there is a relationship
# between the number of players and the amount each player position drinks
# secondarily, to determine how likely one player is to be assigned many more
# drinks than another (via retaining the threeman role)
#
# remember arrays start at zero

def increase_player_turn(player_turn):
  if player_turn == players - 1:
    player_turn = 0
  else:
    player_turn += 1
  return player_turn

def player_drinks(player_turn, direction): # as in "player that drinks"
  player_drinks = 0
  if direction == 1:
    if player_turn == players - 1:
      player_drinks = 0
    else:
      player_drinks = player_turn + 1

  else:
    if player_turn == 0:
      player_drinks = players - 1
    else:
      player_drinks = player_turn - 1

  return player_drinks

def exclusive_random(three_man):
  #select a player to be three_man that isn't the current player
  exclude = [three_man]
  new_three_man = randint(0, players - 1)
  return exclusive_random(three_man) if new_three_man in exclude else new_three_man


def updateBuffer(arrayOfStrings):
    #update output terminal info in place
    arrayLength = len(arrayOfStrings)
    for i in range(arrayLength):
      print(arrayOfStrings[i])
    sleep(0.01)
    bufferControl = '\x1b'+'['+str(arrayLength) +'A' +'\x1b[J'
    print(bufferControl, end="")

def player_display(player_array, player_turn, three_man):
    #print player drink counts with player turn and threeman colored in
    outString = ""
    for i in range(len(player_array)):
      if i == player_turn:
        outString += "\x1b[0;32m" + str(player_array[i]) + "\x1b[0;37m" + " " 
      elif i == three_man:
        outString += "\x1b[0;33m" + str(player_array[i]) + "\x1b[0;37m" + " "
      else:
        outString += str(player_array[i]) + " " 
    
    return outString

def play_full_game(three_man, player_array, player_turn, players, rounds, interactiveDisplay):
  while rounds > 0:
    # roll all the dice and find their sum
    # action = False means no interesting number was rolled
    # if action stays false after the roll, then it becomes
    # the next player's turn
    action = False
    die_one = randint(1,6)
    die_two = randint(1,6)
    die_sum = die_one + die_two

    # if a three is rolled, three man drinks
    # "drink" = player postiion in player array is incremented
    # if a three is rolled by the three man, a new three man is selected
    # (cannot be current three man)
    if die_one == 3 or die_two == 3 or die_sum%3 == 0:
      action = True
      if three_man == player_turn:
        three_man = exclusive_random(three_man)
      player_array[three_man] += 1
      whodrinks = "threeman"

    # if the sum of the dice is seven, the player left
    # of the three man drinks
    if die_sum == 7:
      action = True
      player_array[player_drinks(player_turn, -1)] += 1
      whodrinks = "left of player"

    # if the sum of the dice is eleven, the player right
    # of the three man drinks
    if die_sum == 11:
      action = True
      player_array[player_drinks(player_turn, 1)] += 1
      whodrinks = "right of player"

    # no fun numbers were rolled, so next turn.
    # Since this is only incremented when nothing fun is rolled,
    # it stays one person's turn until they don't roll anything
    if action == False:
      player_turn = increase_player_turn(player_turn)
      whodrinks = "no one"
    
    # end of round, print results if interactiveDisplay enabled
    rounds -= 1

    # interactive display
    if (interactiveDisplay):
      printBuffer=[]
      printBuffer.append("##############")
      printBuffer.append("ROUND: " + str(rounds))
      printBuffer.append("dice: " + str(die_one) + " + " + str(die_two) + " = " + str(die_sum))
      printBuffer.append("action: " + str(action) + '\t' + whodrinks + " drinks")
      printBuffer.append("player display: " + player_display(player_array, player_turn, three_man))
      printBuffer.append("##############")
    
      updateBuffer(printBuffer)


if __name__ == "__main__":
  # initial setup. choose three man randomly and choose
  # who starts. Also initialize players to zero drinks

  parser = argparse.ArgumentParser(description='Get input for game of three man')
  parser.add_argument('players', action='store',
                    help='the number of players')
  parser.add_argument('rounds', action='store',
                    help='the number of rounds')
  parser.add_argument('DataSetSize', action='store',
                    help='the number of datasets generated')
  parser.add_argument('-i', '--interactiveTF', dest='interactiveDisplay', default=False,
                    help='set flag for interactive output while data is generated')
  args = parser.parse_args()

  DataSetSize = int(args.DataSetSize)
  players = int(args.players)
  rounds = int(args.rounds)
  interactiveDisplay = bool(args.interactiveDisplay)

  array_of_arrays = []
  for i in range(DataSetSize):

    three_man = randint(0,players-1)
    player_array = [0 for i in range(players)]
    player_turn = randint(0,players-1)

    play_full_game(three_man, player_array, player_turn, players, rounds, interactiveDisplay)
    array_of_arrays.append(player_array)

# write final results to file as np array

outputFileName = 'players' + str(players) + 'rounds' + str(rounds) + 'OriginalRules.npy'
np.save(outputFileName, array_of_arrays)

