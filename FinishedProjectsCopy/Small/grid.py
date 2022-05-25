import numpy as np
import time

grid = np.random.randint(0,2,size=(5,5))
#print(grid)

size = 11
loops = 10
z_grid = np.zeros((size,size),int)
z_grid[5,5] = 1

z_buff = np.zeros((size,size),int)
while loops > 0:
  print(z_grid)
  time.sleep(2)
  print('\x1b['+str(size)+'A\x1b[J\x1b[1A')
  for i in range(1,size-1):
    for j in range(1,size-1):
      if z_grid[i,j] >= 1:
        # cardinal
        z_buff[i,j-1] += 1
        z_buff[i,j+1] += 1
        z_buff[i-1,j] += 1
        z_buff[i+1,j] += 1
        # diags
        z_buff[i+1,j+1] += 1
        z_buff[i+1,j-1] += 1
        z_buff[i-1,j+1] += 1
        z_buff[i-1,j-1] += 1

        z_grid[i,j] = 0
  z_grid += z_buff
  z_buff -= z_buff
  loops -= 1

"""
a = np.random.randint(0, 5, size =(5,5))
print(a)

b = a < 3
print(b)

c = b.astype(int)
print(c)

d = (a < 3).astype(int)
print(d)
"""
