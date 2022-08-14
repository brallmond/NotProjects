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


def move(xin, yin):
#  for i in range(len(xin)):
#    print(xin[1])
#    xin[1] += 1
#    yin[1] += 1
#    if ((i > 100) and (i < 400)):
#      xin[i+1] += 0.1
#      xin[i-1] += 0.1
#      yin[i+1] += 0.1
#      yin[i-1] += 0.1
  return xin/1.05, yin/1.05


if __name__ == "__main__":

  # make plot interface and random data using np
  fig = plt.subplots(figsize =(6, 5))
  n = 100
  x = np.random.uniform(-1, 1, size=n)  
  y = np.random.uniform(-1, 1, size=n)
  
  plt.ion() # turn on interactive plotting
  # make plot, draw it, make file, save plot to file, pause, clear from figure, update data, and restart loop
  filenames = []
  for i in range(50):
    plt.hist2d(x, y, bins=100, range=[[-1,1],[-1,1]])
    plt.draw()
    filename = f'frame_{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.pause(0.00001)
    plt.clf()
    x, y = move(x, y) # move can be arbitrarily modified for interesting behaviors

  # let plot persist (replot, turn off interactive plot, and show plot)
  plt.hist2d(x, y, bins=n, range=[[-1,1],[-1,1]])
  plt.ioff()
  plt.show()

  # Stich image files together to make a gif, remove the individual file after it's been stitched
  with imageio.get_writer('output.gif', mode='I') as writer:
    for filename in filenames:
      image = imageio.imread(filename)
      writer.append_data(image)
      os.remove(filename)



