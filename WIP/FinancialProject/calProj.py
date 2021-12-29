import calendar

# want date and day of the week

cal = calendar.Calendar(6)
print("6 is Sunday")
monthsDays = []
for month in range(1,12+1):
  for day, weekday in cal.itermonthdays2(2022, month):
    if day != 0:
      monthsDays.append([month,day,weekday])
      #print(month, day)
print(monthsDays)
