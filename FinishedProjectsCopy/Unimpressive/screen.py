import numpy as np
from time import sleep

for i in range(5):
  print(' '*i + str(i) + ' '*(5-i-1) + "#")
  sleep(0.35)
  print('\x1b[A' + '\x1b[2K' + '\x1b[A')
for i in range(4,0,-1):
  print(' '*i + str(i) + ' '*(5-i-1) + "#")
  sleep(0.35)
  print('\x1b[A' + '\x1b[2K' + '\x1b[A')
