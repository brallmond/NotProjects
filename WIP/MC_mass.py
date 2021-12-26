import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random as rand

# data yielding func
def gen(x, y, z, ux, uy, uz, s, th, fi):
  sinth = np.sin(th)
  costh = np.cos(th)
  sinfi = np.sin(fi)
  cosfi = np.cos(fi)
  sqrz = np.sqrt(1-uz*uz)

  uxp = (sinth*(ux*uz*cosfi-uy*sinfi)/sqrz) + ux*costh
  uyp = (sinth*(uy*uz*cosfi+ux*sinfi)/sqrz) + uy*costh
  uzp = -1*sqrz*sinth*cosfi + uz*costh

  x += s*uxp
  y += s*uyp
  z += s*uzp

  return x, y, z

def shoot(x, y, z, ux, uy, uz, s, th, fi, w)
  
def update(data):
  t, x, y = data
  xdata.append(x)
  ydata.append(y)

  line.set_data(xdata, ydata)
  head.set_data(x, y)
  return holder

if __name__ == "__main__"
  #init conds
  x = 0
  y = 0
  z = 0
  ux = 0
  uy = 0
  uz = 1

  ab = 0.5
  sc = 0.5
  
  tot = ab + sc
  xsi = rand.uniform(0.0, 1.0)
  s = -1*np.log(xsi)/tot
  fi = 2*3.14159265359*xsi
  g = 0 #anisotropy
  th = np.acos(1-2*xsi)
  
  A = 1
  fig = plt.figure()
  ax = plt.axes(xlim=(-A, A), ylim=(-A, A))
  ax.grid()
  ax.set_aspect('equal')
  plt.title("MC packet propagation")

  xdata, ydata, xpoint, ypoint = [], [], [], []
  line, = ax.plot(xdata, ydata, lw=2, color='black')
  head, = ax.plot(xpoint, ypoint, color='red', marker='o', markeredgecolor='r')
  holder = [line, head]

  ani = anim.FuncAnimation(fig, update, gen(x, y, z, ux, uy, uz, s, th, fi), blit=True, interval = 50, repeat=False)
