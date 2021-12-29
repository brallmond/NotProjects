import calendar

cal = calendar.Calendar(6)
print("6 is Sunday")
fullCalendar = []
for month in range(1,12+1):
  for day, weekday in cal.itermonthdays2(2022, month):
    if day != 0:
      fullCalendar.append((month,day,weekday))

# make list of static charges from csv
import pandas
df = pandas.read_csv('DaysAndCharges.csv')
listOfDays = df["Day"].tolist()
listOfCharges = df["Charge"].tolist()
recurringCharges = [(listOfDays[i], float(listOfCharges[i])) for i in range(0,len(listOfDays))]
#print(recurringCharges)

# anticipated one-time costs
oneTimeExpenses = [(1,20,-500)]

# averaged weekly expenses
groceryWeeklyCost = 50
restarauntWeeklyCost = 28
coffeeWeeklyCost = 12

# options, add arg parse w defaults for paycheck
balance = 3000.
paycheckAmt = 797.43
paycheckDay = 7
paycheckMonth = 1
firstPayCheck = True
addWeeklyExpenses = False

for month, day, weekday in fullCalendar:

  if month > 5: break

  # recurring charges
  for dayRC, chargeRC in recurringCharges:
    if dayRC == day:
      balance += chargeRC  

  # paychecks
  if ( (weekday == 4) and (not firstPayCheck) ):
    fridayCount += 1
    if (fridayCount == 2):
      balance += paycheckAmt
      fridayCount = 0
  if ( (month == paycheckMonth) and (day == paycheckDay) and (firstPayCheck) ): # first paycheck of the year jan 7th
    fridayCount = 0
    firstPayCheck = False
    balance += paycheckAmt

  # weekly predicted costs
  # grocery avg is 200 per month
  # restraunt avg is 150 per month
  # ignoring coffee avg (we're significantly reducing it)
  if (addWeeklyExpenses):
    # every Sunday, $40 at dillons for groceries
    if (weekday == 6): balance -= groceryWeeklyCost
    # every Monday, $20 at AJs for beer, $8 for union lunch on Fridays
    if (weekday == 0): balance -= restarauntWeeklyCost
    # every Tuesday, $12 for avg weekly coffees
    if (weekday == 1): balance -= coffeeWeeklyCost
  
  # anticipated one time costs
  for monthOTE, dayOTE, chargeOTE in oneTimeExpenses:
    if ( (monthOTE == month) and (dayOTE == day) ):
      balance += chargeOTE

  # print output each day
  print("{} {}: {:.2f}".format(month, day, balance))
