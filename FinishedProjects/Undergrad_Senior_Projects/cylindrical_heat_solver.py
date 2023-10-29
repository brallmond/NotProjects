import numpy as np

#animator import
import matplotlib 
matplotlib.use("Agg") 
filenames = []

import matplotlib.pyplot as plt

class rzgrid(object):
  """
  Create an object in the r and z directions
  containing environment dimensions, cell areas, and cell heat values.
  ns is used as shorthand for ’North/South’ meaning upward and downward directions, or above and below
  ew is used in a similar way
  """
  def __init__(self, rlen, zlen, rcellnumber, zcellnumber, ambient_temp): 
    self.ambient_temp = ambient_temp
    self.rlen = rlen*1.0
    self.zlen = zlen*1.0
    self.rcellnumber = rcellnumber
    self.zcellnumber = zcellnumber

    #prefill the ’vals’ cells which contains heat data
    self.ambient_temp = ambient_temp
    self.vals = np.full((self.rcellnumber, self.zcellnumber), self.ambient_temp)

    #annular disks
    self.ns_width = [(np.pi*(((self.rlen/self.rcellnumber)*(i+1))**2
                       -((self.rlen/self.rcellnumber)*i)**2))
                       for i in range(self.rcellnumber+1)]

    #area of rectangle from a cylinder
    self.ew_width = [2.0*np.pi*(self.rlen/self.rcellnumber)*(i+1)
                        *(self.zlen/self.zcellnumber) 
                        for i in range(self.zcellnumber+1)]

  def set(self, r, z, val): 
    self.vals[r, z] = val

class heater(object):
  """ 
  Create an environment to manipulate a defined grid of values, 
  imported in the __init__ statement,
  and operated on by subsequent functions.
  """
  def __init__(self, grid): 
    self.grid = grid
  def norm_flux(self, ew_loc, ns_loc, val): 
    self.side_e = 0
    self.side_n=0
    self.side_w = 0
    self.side_s = 0
    self.sum_sides = 0
    self.end_w = self.grid.rcellnumber 
    self.end_n = self.grid.zcellnumber
    self.ew_loc = ew_loc 
    self.ns_loc = ns_loc 
    self.val = val

    #dont calculate fluxes for cells outside of environment
    if (self.ew_loc != 0):
      self.side_e =-self.val + self.grid.vals[ew_loc-1][ns_loc]
    if (self.ns_loc != self.end_n-1):
      self.side_n =-self.val + self.grid.vals[ew_loc][ns_loc+1]
    if (self.ew_loc != self.end_w-1):
      self.side_w =-self.val + self.grid.vals[ew_loc+1][ns_loc]
    if (self.ns_loc != 0):
      self.side_s =-self.val + self.grid.vals[ew_loc][ns_loc-1]

    self.sum_sides = (self.side_e + self.side_w)/self.grid.ew_width[self.ew_loc] 
    self.sum_sides += (self.side_n + self.side_s)/self.grid.ns_width[self.ns_loc] 
    return self.sum_sides


  def ex_step(self, dt):
    """
    An explicit euler solver works by getting
    an estimate of a value, then adding a small portion of that value (dt) 
    to the original estimate and reestimating. Doing this a few times, 
    and getting kind of fancy with the math, you
    can often get a pretty decent estimate, although
    this becomes increasingly computationally taxing.
    """
    self.dt = dt
    self.copy_vals = self.grid.vals
    for i in range(self.grid.rcellnumber):
      for j in range(self.grid.zcellnumber): 
        self.val = 0
        self.val = self.grid.vals[i,j]
        self.p_val = 0
        self.p_val = self.norm_flux(i, j, self.val) 
        self.val += self.p_val*self.dt
        #value assigned to a copy of cells first so all cells 
        #are incremented by the same time step when all 
        #cells are reassigned to the values in the copy
        self.copy_vals[i, j] = self.val
    self.grid.vals = self.copy_vals

def total(self):
  """
  Function to compute the total amount
  of heat in the environment.
  """
  self.total=0
  for i in range(self.grid.rcellnumber):
    for j in range(self.grid.zcellnumber): 
      self.total += self.grid.vals[i,j]
  return self.total

#define a mesh and working environment
rlen = 1.25
zlen = 1.25 
rcellnumber = 10 
zcellnumber = 10 
ambient_temp = 20.0

mesh = rzgrid(rlen, zlen, rcellnumber, zcellnumber, ambient_temp)
sim = heater(mesh)

def plot(array, i):
  it = str(i)
  plt.title(it)
  plt.imshow(array.T, cmap = plt.cm.hot, interpolation = "nearest")
  # animator s t u f f
  plt.colorbar()
  plt.savefig("./Heater/" + it)
  filenames.append("./Heater/" + it + ".png")
  #plt.show()
  plt.close()

#main loop
iteration_count = 200
for i in range(iteration_count):
  #plot generates a heat map
  #graph.append saves a copy of the array
  #and stores it for use in a gif
  plot(sim.grid.vals.T, i)
  #graph.append(sim.grid.vals[0, 0])
  #step sim forward in time
  sim.ex_step(0.015)
  #condition to start origin with initial temp
  if i==0:
    mesh.set(0, 0, 100)

#creates gif from graphs saved earlier
import imageio
images = []
for filename in filenames:
  images.append(imageio.imread(filename)) 
  imageio.mimsave("./Heater/Heater.gif", images)








