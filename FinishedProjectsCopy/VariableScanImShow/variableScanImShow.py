# Braden Allmond - July 2nd, 2022
# Testing plotting approach for a scan of three variables on 
# data consisting of four entries.

# Including useful math and plotting packages
import numpy as np
import matplotlib.pyplot as plt

# Including function to get data
# from this guide
# https://stackoverflow.com/questions/2349991/how-can-i-import-other-python-files
from data.realData import getData

# Initializing variable space, like whole numbers
w = np.linspace(10, 14, 3) # 10, 12, 14
x = np.linspace(30, 50, 11) 
y = np.linspace(300, 500, 11)

# Getting real data
big_foo = getData()


# Initiate grid to be filled with counts
zz = np.zeros((3,11,11))

# Iterate over all three variables in nested for-loops
# use enumerate to make index:value pairs so we can
# compare to a value and use that value's index at the same time
for i, wentry in enumerate(w):
  for j, xentry in enumerate(x):
    for k, yentry in enumerate(y):
      # Iterate over the data
      for l in range(len(big_foo)):
        roo = big_foo[l]
        if ((roo[3] > wentry) and (roo[0] > xentry and roo[1] > xentry) and (roo[2] > yentry)):
          #print(wentry, xentry, yentry)
          zz[i,j,k] += 1

# zz is now filled with counts (i.e. if the data satisfies the condition of a zz-cell, increment that cell's value)
#print(zz)

# plotting from
# https://stackoverflow.com/questions/13784201/how-to-have-one-colorbar-for-all-subplots
# and
# https://stackoverflow.com/questions/41793931/plotting-images-side-by-side-using-matplotlib
# and
# https://stackoverflow.com/questions/9295026/matplotlib-plots-removing-axis-legends-and-white-spaces

# Make copies of x and y linspaces but as integers (for plotting)
intx = [int(i) for i in x]
inty = [int(i) for i in y]

# Find the maximum grid element and add a small amount, use this value as vmax when plotting
gridmax = np.max(zz) + 2

# Make 3 subplots in a horizontal line
fig, axes = plt.subplots(1, 3)
fig.set_size_inches(10.5, 10.5)

for i, ax in enumerate(axes.flat):
  # origin='lower' makes the output image cartesian instead of the default image format
  im = ax.imshow(zz[i], vmin=0, vmax=gridmax, cmap = 'copper', interpolation='nearest', origin='lower')
  ax.set_title("electronPt " + str(2*(i) + 10), fontsize=8)
  ax.set_xlabel('jetPt')
  ax.set_ylabel('mjj')

  # Get start and end of x-axis for tick-mark position info
  # y-axis has same dimension and positions in our case
  start, end = ax.get_xlim()

  # Set tick locations explicitly and then assign new tick labels for x- and y-axes
  ax.xaxis.set_ticks(np.arange(start+0.5, end, 1))
  ax.xaxis.set_ticklabels(intx)
  ax.yaxis.set_ticks(np.arange(start+0.5, end, 1))
  ax.yaxis.set_ticklabels(inty)

  # Put the numerical value of the grid in the grid location
  # this removes the need for a colorbar (which was too difficult for me to format)
  for (n,m),label in np.ndenumerate(zz[i]):
    ax.text(m,n,int(label), ha='center', va='center', color='white', fontsize=6)

  # Only let the y-axis on the first (leftmost) plot be visible
  if (i != 0):
    ax.get_yaxis().set_visible(False)

# Save a pdf of your plot
plt.savefig('output.pdf')
print("If it looks bad, try going full-screen")
plt.show()




