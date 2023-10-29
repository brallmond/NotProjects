import numpy as np 
import random

#animator import
import matplotlib 
matplotlib.use("Agg") 
filenames = []

import matplotlib.pyplot as plt

# function to plot crystal , currently using gray color mapping
def plot(array, i): 
  it = str(i)
  plt.title(it)
  plt.imshow(array.T, cmap = plt.cm.bone, interpolation = "nearest", vmax = 1)
  # animator s t u f f
  plt.colorbar()
  plt.savefig("./Lattice/" + it) 
  filenames.append("./Lattice/" + it + ".png")
  plt.close()

class lattice(object):
  def __init__ (self, size, TOL):
    self.size = size
    # makes crystal tols [0.5 , 1.5 , 2.5 , 3.5] for
    self.TOL = [TOL, 1+TOL, 2+TOL, 3+TOL]
    # makes a square grid to move around
    self.grid = np.zeros((size,size))
    # ”types” will always need zero type
    self.types = [0,1,2,3,4]
    self.pop = [2000, 650, 90]

  def seeding(self, k, l, type_c):
    # makes location grid [k, l ] a seed/starter location
    self.type_c = type_c
    self.grid[k,l] = self.types[self.type_c]

  def generation(self):
    for i in range(1,self.size-1):
      for j in range(1,self.size-1):
        # the first two loops go thru all grid locations
        for k in range(len(self.TOL)):
          # the last loop goes thru different crystal types
          base = self.types[k]
          base_up = self.types[k+1]
          # meat and potatoes . two lines above give limit of range
          # booleans below say generate a random value if a crystal of 
          # current type is deteced , provided that higher types aren’t 
          # already filling the cardinal spaces surrounding it
          if self.grid[i,j] == base_up:
            if self.grid[i+1,j] < base_up:
              self.grid[i+1,j] = base + random.random() 
            if self.grid[i-1,j] < base_up:
              self.grid[i-1,j] = base + random.random() 
            if self.grid[i,j+1] < base_up:
              self.grid[i,j+1] = base + random.random() 
            if self.grid[i,j-1] < base_up:
              self.grid[i,j-1] = base + random.random()

  def formation(self):
    for i in range(1,self.size-1):
      for j in range(1,self.size-1):
        for k in range(len(self.TOL)):
        # if the grid value is above tolerance, it turns into a crystal
          if self.TOL[k] < self.grid[i,j] < self.TOL[k+1] and self.pop[k] > 0: 
            self.grid[i,j] = self.types[k+1]
            self.pop[k] -= 1
          else : pass

  def check(self, check_TOL):
    # ends sim if a tolerable number of grids hold crystals
    self.check_TOL = check_TOL 
    check = 0
    check_BOOL = True
    for i in range(1,self.size-1):
      for j in range(1,self.size-1): 
        if self.grid[i,j] < 1:
          check += 1
    if check > self.check_TOL:
      check_BOOL = False 
    return check_BOOL

#if your threshold is too low you don’t get very interesting behavior
c = lattice(5,0.95)
c.seeding (2 ,2 ,1)

i=0
lag = 90
cutoff = 10
filled = False 
while i < cutoff :
  plot(c.grid, i) 
  i += 1
  c.generation() 
  c.formation()
  if (c.check(100) == True and filled != True): 
    cutoff = i + lag
    filled = True

import imageio
images = []
for filename in filenames :
  images.append(imageio.imread(filename)) 
  imageio.mimsave("./Lattice/Lattice.gif", images)
print("gif created")




