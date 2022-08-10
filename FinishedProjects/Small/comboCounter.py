# used for SAP first turn animal combination countings

digits = 9

def IsConditionMet(numberString_, conditionVal_, conditionValTimes_, inclusive_, output_):
  conditionInStringCount = numberString_.count(str(conditionVal_))

  if (inclusive_):
    if (conditionInStringCount >= conditionValTimes_):
      if (output_): print(numberString_)
      return 1
    else: return 0

  if (not inclusive_):
    if (conditionInStringCount == conditionValTimes_):
      if (output_): print(numberString_)
      return 1
    else: return 0

def IsConditionMetOr(numberString_, conditionVal1_, conditionVal2_, conditionValTimes_, inclusive_, output_):
  condition1InStringCount = numberString_.count(str(conditionVal1_))
  condition2InStringCount = numberString_.count(str(conditionVal2_))

  if (inclusive_):
    if (condition1InStringCount >= conditionValTimes_):
      if (output_): print(numberString_)
      return 1
    else: return 0

  if (not inclusive_):
    if ( (condition1InStringCount == conditionValTimes_) & (condition2InStringCount == conditionValTimes_) ):
      if (output_): print(numberString_)
      return 1
    else: return 0


hasOutput = True
isInclusive = False
conditionVal = 7

three = False
six = True
  
if (three):
  conditionMetCount = 0
  conditionValTimes = 3
  for i in range(digits):
    for j in range(digits):
      for k in range(digits):
        numberString = str(i) + str(j) + str(k)
        conditionMetCount += IsConditionMet(numberString, conditionVal, conditionValTimes, isInclusive, hasOutput)
  print(conditionMetCount)

if (six):
  for conditionValTimes in range(3, 6+1):
    conditionMetCount = 0
    for i in range(digits):
      for j in range(digits):
        for k in range(digits):
          for l in range(digits):
            for m in range(digits):
              for n in range(digits):
                numberString = str(i) + str(j) + str(k) + str(l) + str(m) + str(n)
                #conditionMetCount += IsConditionMet(numberString, conditionVal, conditionValTimes, isInclusive, hasOutput)
                conditionMetCount += IsConditionMetOr(numberString, conditionVal, conditionVal+1, conditionValTimes, isInclusive, hasOutput)
    print("found {} {}'s {} times".format(conditionValTimes, conditionVal, conditionMetCount))
    #print(conditionMetCount)
