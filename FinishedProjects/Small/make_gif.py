import numpy as np
import matplotlib.pyplot as plt
import os
#import imageio
import imageio.v2 as imageio


if __name__ == "__main__":

  #path = "/home/braden/Pictures/DCIM/Pre Run Shotgun"
  path = "/home/braden/Pictures/Screenshots"
  filenames = os.listdir(path)
  filenames.sort()
  #print(filenames)
  full_filenames = []
  for filename in filenames:
    filename = path + '/' + filename
    full_filenames.append(filename)

  images = list(map(lambda temp_filename: imageio.imread(temp_filename), full_filenames))

  imageio.mimsave(os.path.join('output.gif'), images, duration = 0.13)

  #with imageio.get_writer('output.gif', mode='I') as writer:
  #  for filename in filenames:
  #    filename = path + '/' + filename
  #    image = imageio.imread(filename)
      #full_tuple = image.shape
      #print(filename, full_tuple, full_tuple[0]/float(full_tuple[1]))
  #    writer.append_data(image)

