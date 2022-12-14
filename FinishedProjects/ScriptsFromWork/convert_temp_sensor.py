import sys

def chip_and_channel_to_label(user_chip, user_channel):
    label = user_chip*6 + user_channel + 1
    return label


def label_to_chip_and_channel(user_label):
    label_minus_one = user_label - 1
    channel_id = (label_minus_one % 6)
    chip_id = (label_minus_one - channel_id) / 6 
    return (int(chip_id), channel_id)

if __name__ == "__main__":

  nargs = len(sys.argv) - 1

  segments = {
    #0 : ["not used"],
    1 : [24, 15, 9, 4, 11, 2],
    2 : [14, 17, 6, 5, 9, 7],
    3 : [21, 10, 12, 11, 1, 3],
    4 : [22, 23, 7, 8, 12, 19],
    5 : [20, 10, 5, 9, 8, 4],
  }

  rows = {
    1 : [24, 14, 21, 22, 20], # top
    2 : [15, 17, 10, 23, 10], # first from top
    3 : [3, 6, 12, 7, 5],     # second from top
    4 : [4, 5, 11, 8, 9],     # second from bottom
    5 : [11, 9, 1, 12, 8],    # first from bottom
    6 : [2, 7, 3, 19, 4],     # bottom
  }

  on_tray = {
    1 : [15, 13, 14, 17, 18, 19], # on segment zero
    2 : [15, 17, 24, 22],         # row top center
    3 : [14, 19, 6],              # row bottom (incomplete)
    4 : [16, 21],                 # exposed CO2 pipe
  }

  corners = {
    1 : [14, 2, 19, 20, 22, 21], # compare front-back corners
    2 : [20, 21, 22],            # back corner
  }

  ambient = {
    1 : [18, 13, 16], # ambient
  }

  groups = ambient

  if (nargs == 0):
    for grouping_number in groups:
      print(f" {grouping_number}, labels : {groups[grouping_number]}")
      for label in groups[grouping_number]:
        chip_id, channel_id = label_to_chip_and_channel(label)
        print(f" CHIP ID : {chip_id},   CHANNEL_ID : {channel_id}")

  elif (nargs == 1):
    chip_id, channel_id = label_to_chip_and_channel(int(sys.argv[1]))
    print(f" CHIP ID : {chip_id},   CHANNEL_ID : {channel_id}")

  elif (nargs == 2):
    label = chip_and_channel_to_label(int(sys.argv[1]), int(sys.argv[2]))
    print(f" LABEL : {label}")

