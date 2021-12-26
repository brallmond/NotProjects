import random as rand

# remember arrays start at zero

players = 5
rounds = 10

def increase_player_turn(player_turn):
  if player_turn == players - 1:
    player_turn = 0
  else:
    player_turn += 1
  return player_turn

def player_drinks(player_turn, direction):
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
  exclude = [three_man]
  new_three_man = rand.randint(0, players - 1)
  return exclusive_random(three_man) if new_three_man in exclude else new_three_man

if __name__ == "__main__":
  # initial setup. choose three man randomly and choose
  # who starts. Also initialize players to zero drinks
  three_man = rand.randint(0,players-1)
  player_array = [0 for i in range(players)]
  player_turn = rand.randint(0,players-1)

  print("three man = {}".format(three_man))
  print("you start! {}".format(player_turn))

  while rounds > 0:
    # roll all the dice and find their sum
    # action = False means no interesting number was rolled
    # if action stays false after the roll, then it becomes
    # the next player's turn
    action = False
    die_one = rand.randint(1,6)
    die_two = rand.randint(1,6)
    die_sum = die_one + die_two

    # if a three is rolled, three man drinks
    # "drink" = player array is incremented
    # if a three is rolled by the three man, a new three man is selected
    # (cannot be current three man)
    if die_one == 3 or die_two == 3 or die_sum == 3:
      action = True
      if three_man == player_turn:
        three_man = exclusive_random(three_man)
      player_array[three_man] += 1

    # if the sum of the dice is seven, the player left
    # of the three man drinks
    if die_sum == 7:
      action = True
      player_array[player_drinks(player_turn, -1)] += 1

    # if the sum of the dice is eleven, the player right
    # of the three man drinks
    if die_sum == 11:
      action = True
      player_array[player_drinks(player_turn, 1)] += 1

    # no fun numbers were rolled, so next turn.
    # Since this is only incremented when nothing fun is rolled,
    # it stays one person's turn until they don't roll anything
    if action == False:
      player_turn = increase_player_turn(player_turn)
    
    rounds -= 1
    print("##############")
    print(die_one, die_two, die_sum)
    print(player_array)
    print("your turn! {}".format(player_turn))
    print("##############")
