import pandas
import numpy
df = pandas.read_csv('example.csv')
dfArray = df.values.tolist()
print(df.values.tolist())
# start available, end available, start good, end good
# [1, 163, 63, 100]
#[[1, 163, 63, 100], [2, 45, 4, 70], [1, 244, 66, 244], [50, 423, 1, 200]]
# given the following info, we want to output only the ranges
# which are good and available
# i.e. for the first entry we want [63, 100]

outputGA = [] # output good and available
for i in range(len(dfArray)):
  workingList = dfArray[i]
  startAvail = workingList[0]
  endAvail = workingList[1]
  startGood = workingList[2]
  endGood = workingList[3]
  containerGA = []
  startGA = -1
  endGA = -1

  # only do full logic with good rows  
  if ((startGood < endAvail) & (endGood > startAvail)):
    if (startGood >= startAvail):
      startGA = startGood
    else: startGA = startAvail

    if (endGood <= endAvail):
      endGA = endGood
    else: endGA = endAvail

  containerGA.append(startGA)
  containerGA.append(endGA) 
  outputGA.append(containerGA)

print(outputGA)
