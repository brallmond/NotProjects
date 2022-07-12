import numpy as np
import sys
import matplotlib.pyplot as plt

inFile = sys.argv # all input arguments in an array

output = np.load(str(inFile[1]))
output_size = len(output)

maxes = np.empty((100,1))
mins = np.empty((100,1))
means = np.empty((100,1))
variances = np.empty((100,1))

print("MAX" + '\t' + "MIN" + '\t' + "MEAN" + '\t' + "VAR")
for i in range(output_size):
  maxes[i] = np.max(output[i])
  mins[i] = np.min(output[i])
  means[i] = np.mean(output[i])
  variances[i] = np.var(output[i])
  #print(maxes[i], mins[i], means[i], variances[i])
  #print(str(np.max(output[i])) + '\t' + str(np.min(output[i])) + '\t' \
  #    + str(np.mean(output[i])) + '\t' + str(np.var(output[i])))
 
fig = plt.figure()
ax_maxes = fig.add_subplot(1,2,1)
ax_mins = fig.add_subplot(1,2,2)

n, bins, patches = ax_maxes.hist(maxes)
ax_maxes.set_title("Maximum Number of Drinks")
ax_maxes.set_xlabel("Number of Drinks")
ax_maxes.set_ylabel("Number of Times Assigned")

n, bins, patches = ax_mins.hist(mins)
ax_mins.set_title("Minimum Number of Drinks")
ax_mins.set_xlabel("Number of Drinks")
ax_mins.set_ylabel("")

plt.show() 
