import numpy as np
import matplotlib.pyplot as plt
import random as rand

if __name__ == "__main__":
  reps = 0
  #init conds
  x, y, z, ux, uy = 0.0, 0.0, 0.0, 0.0, 0.0
  uz = 1.0
  ab = 0.5
  sc = 0.5
  w = 1.0

  tot = ab + sc
  
  #fig stuff
  plt.ion()
  plt.xlim(-10, 10)
  plt.ylim(-10, 10)
  xlist, ylist, zlist = [], [], []
  while (w > 0.0001 and reps < 25):
    xsi = rand.uniform(0.0, 1.0)
    s = -1.0*np.log(xsi)/tot
    fi = 2.0*3.14159*xsi
    th = np.arccos(1-2*xsi)

    sinth = np.sin(th)
    costh = np.cos(th)
    sinfi = np.sin(fi)
    cosfi = np.cos(fi)
    sqrz = np.sqrt(1.0 - (uz*uz-0.0001))
    
    if (uz == 1.0 or uz == -1.0):
      uxp = sinth*cosfi
      uyp = uz*sinth*sinfi
      uzp = uz*costh
    else:
      uxp = (sinth*(ux*uz*cosfi-uy*sinfi)/sqrz) + ux*costh
      uyp = (sinth*(uy*uz*cosfi+ux*sinfi)/sqrz) + uy*costh
      uzp = -1.0*sqrz*sinth*cosfi + uz*costh

    ux = uxp
    uy = uyp
    uz = uzp
 
    x += s*ux
    y += s*uy
    z += s*uz

    w -= (ab/tot)*w
    
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)
    print(w)
    reps += 1
    plt.plot(xlist,zlist,'g-')
    plt.draw()
    plt.pause(0.1)
