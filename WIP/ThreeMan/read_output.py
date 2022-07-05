import numpy as np
import sys

inFile = sys.argv # all input arguments in an array

output = np.load(str(inFile[1]))
output_size = len(output)

for i in range(output_size):
  print(np.max(output[i]))


# sum all output arrays and display 
#
# report max and min?
#
# variance?
