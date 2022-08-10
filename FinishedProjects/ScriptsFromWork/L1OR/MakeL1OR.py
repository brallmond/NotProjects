import pandas
import numpy
df = pandas.read_csv('PSequal1.csv')
listOfL1s = df["Name"].tolist()
print(listOfL1s)

megaOR = ' || '.join(listOfL1s)

print(megaOR)
