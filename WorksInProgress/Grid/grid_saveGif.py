import numpy as np
import matplotlib.pyplot as plt
import os
import imageio

# using this site
# https://www.geeksforgeeks.org/plot-2-d-histogram-in-python-using-matplotlib/
# used this stackoverflow for updating originally
# https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
# look at this site for saving a gif
# https://towardsdatascience.com/basics-of-gifs-with-pythons-matplotlib-54dd544b6f30

# in principle, the "move" function can be modified for different interesting cases/behaviors
# the main parts of this script are interacting with the plotting tools correctly, but once it's
# set it's more or less brainless

# saving a gif is different from interactively updating it, so there's a different script for it

def move(xin, yin):
  for i in range(len(xin)):
    if ((i > 100) and (i < 400)):
      xin[i+1] += 1
      xin[i-1] += 1
  return xin, yin

if __name__ == "__main__":

  # make plot interface and random data
  fig = plt.subplots()
  n = 1000
  x = np.random.uniform(-1, 1, size=n)  
  y = np.random.uniform(-1, 1, size=n)
  
  # plot data, save as a generic image file and save the name. update data at end
  filenames = []
  for i in range(50):
    plt.hist2d(x, y, bins=100, range=[[-1,1],[-1,1]])
    filename = f'images/frame_{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()
    x, y = move(x, y)

  # Stich image files together to make a gif
  with imageio.get_writer('Gifs/stars.gif', mode='I') as writer:
      for filename in filenames:
          image = imageio.imread(filename)
          writer.append_data(image)
  # Remove files
  for filename in set(filenames):
      os.remove(filename)
  

  
