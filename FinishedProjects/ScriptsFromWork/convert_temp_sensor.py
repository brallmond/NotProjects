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

  if (nargs == 0):
    for segment_number in segments:
      print(f"segment {segment_number}, labels : {segments[segment_number]}")
      for label in segments[segment_number]:
        chip_id, channel_id = label_to_chip_and_channel(label)
        print(f" CHIP ID : {chip_id},   CHANNEL_ID : {channel_id}")

  elif (nargs == 1):
    chip_id, channel_id = label_to_chip_and_channel(int(sys.argv[1]))
    print(f" CHIP ID : {chip_id},   CHANNEL_ID : {channel_id}")

  elif (nargs == 2):
    label = chip_and_channel_to_label(int(sys.argv[1]), int(sys.argv[2]))
    print(f" LABEL : {label}")

