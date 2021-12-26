# make "calendar"
dec = [1200 + i for i in range(31)]
jan = [100 + i for i in range(31)]
feb = [200 + i for i in range(28)]
mar = [300 + i for i in range(31)]
apr = [400 + i for i in range(30)]
may = [500 + i for i in range(31)]
jun = [600 + i for i in range(30)]
months = dec + jan + feb + mar + apr + may + jun

# make list of static charges from csv
import pandas
df = pandas.read_csv('DaysAndCharges.csv')
listOfDays = df["Day"].tolist()
listOfCharges = df["Charge"].tolist()
dayCharges = [(listOfDays[i], float(listOfCharges[i])) for i in range(0,len(listOfDays))]

# make list of paydays
payDayIndex = months.index(1210) # most recent payday
payDays = []
for i in range(14): # 14 paychecks, 7 months
  payDays.append(months[payDayIndex])
  payDayIndex += 14 # two weeks

# given monthly averages, make list of dynamic charges
groceryAvg = 200
coffeeAvg = 70
restrauntAvg = 150
lumpExpenses = groceryAvg + coffeeAvg + restrauntAvg

# should i add all charges/credits together in one large list? that would make the main loop simpler

# sum up pay days and charges using current balance and starting date
startBal = 2564
runTotal = startBal
startDate = 1213
startIndex = months.index(startDate)
endDate = 600
endIndex = months.index(endDate)
for date in months:
  # update date, check if it's after the starting date
  currentIndex = months.index(date)
  if currentIndex < startIndex: continue 
  if currentIndex > endIndex: break

  # loop over charges
  for chargeDay, charge in dayCharges:
    if date%100 == chargeDay:
      runTotal += charge

  # loop over paydays
  for payDay in payDays:
    if date == payDay:
      runTotal += 797.43

  if date%100 == 0:
    runTotal -= lumpExpenses

  # display date and expected balance
  print("{}: {:.2f}".format(date,runTotal))


