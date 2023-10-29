from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from math import cos , sin , pi

def woah(f, th, B, q, m):
  x,y,u,v=f
  ddt = [u, v, -1*B*q*(1./m)*v, B*q*(1./m)*u]
  return ddt

B=3.0
q=0.25
m=1.0

x0 = cos(0)
y0 = sin(0)
vx0 = -1*sin(0)
vy0 = cos(0)
f0 = [x0, y0, vx0, vy0]

th = np.linspace(0,8*pi,404)

sol = odeint(woah, f0, th, args=(B,q,m))

fig0 = plt . figure ()
plt.plot(th, sol[:,0], "b", label = "pos X")
plt.plot(th, sol[:,1], "g", label = "pos Y")
plt.plot(th, sol[:,2], "r", label = "veloc X") 
plt.plot(th, sol[:,3], "ro", label = "veloc Y")

plt.legend( loc="best" )
plt.grid()

fig1 = plt.figure ()
plt.plot(sol[:,0],sol[:,1],"ro")
plt.axis("equal")
plt.grid()
plt.show()
