import numpy as np
import sys
import argparse
import matplotlib.pyplot as plt



parser = argparse.ArgumentParser(description='Get input for game of three man')
parser.add_argument('inFile', action='store',
                    help='the file to summarize')
parser.add_argument('-g', '--graphsTF', dest='graphsTF', default=True,
                    help='turn graphs on/off')
parser.add_argument('-p', '--printToTeminalTF', dest='printTerminalTF', default=False,
                    help='print each round\'s stats to terminal')
args = parser.parse_args()

# load data file
inFile = args.inFile
output = np.load(str(inFile))
output_size = len(output)

# set flags
EnableGraphs = args.graphsTF
PrintPerRoundOutput = args.printTerminalTF

# initialize containers
maxes = np.empty((100,1))
mins = np.empty((100,1))
means = np.empty((100,1))
variances = np.empty((100,1))

# fill containers for graphs, optionally print output per dataset
for i in range(output_size):
  maxes[i] = np.max(output[i])
  mins[i] = np.min(output[i])
  means[i] = np.mean(output[i])
  variances[i] = np.var(output[i])
  if PrintPerRoundOutput:
    print("MAX: {0:>4}, MIN: {1:>4}, AVG: {2:>5}, VAR: {3:>4}"\
          .format(maxes[i][0], mins[i][0], means[i][0],variances[i][0]))
 
# make and title container for graphs
fig, axes = plt.subplots(2, 2)
fig.suptitle("Data Summary from Three Man Games in File\n {}".format(inFile))

# below, n is the data, bins are the starting points of the histograms, patches is some figure thing
axes[0][0].title.set_text("maxes")
n, bins, patches = axes[0][0].hist(maxes, color='blue', ec='black', lw=1)

axes[0][1].title.set_text("mins")
n, bins, patches = axes[0][1].hist(mins, color='green', ec='black', lw=1)

axes[1][0].title.set_text("averages")
n, bins, patches = axes[1][0].hist(means, color='orange', ec='black', lw=1)

axes[1][1].title.set_text("variances")
n, bins, patches = axes[1][1].hist(variances, color='purple', ec='black', lw=1)

# make subplot titles not overlap
# https://www.geeksforgeeks.org/how-to-set-the-spacing-between-subplots-in-matplotlib-in-python/
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.85, \
                    wspace=0.4, hspace=0.4)

print("Max of Maxes: {}".format(np.max(maxes)))

#fig = plt.figure()
#ax_maxes = fig.add_subplot(1,2,1)
#ax_mins = fig.add_subplot(1,2,2)
#ax_means = fig.add_subplot(2,2,1)
#ax_variances = fig.add_subplot(2,2,2)
#
#n, bins, patches = ax_maxes.hist(maxes, color='blue', ec='black', lw=1)
#ax_maxes.set_title("Maximum Number of Drinks")
#ax_maxes.set_xlabel("Number of Drinks")
#ax_maxes.set_ylabel("Number of Times Assigned")
#
#n, bins, patches = ax_mins.hist(mins, color='green', ec='black', lw=1)
#ax_mins.set_title("Minimum Number of Drinks")
#ax_mins.set_xlabel("Number of Drinks")
#ax_mins.set_ylabel("")
#
#n, bins, patches = ax_means.hist(maxes, color='orange', ec='black', lw=1)
#ax_means.set_title("Average Number of Drinks")

#n, bins, patches = ax_variances.hist(maxes, color='purple', ec='black', lw=1)
#ax_variances.set_title("Measured Variance between Player Drinks")

plt.show() 
