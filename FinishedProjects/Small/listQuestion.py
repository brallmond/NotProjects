
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]      

PassConditionA =  [i for i in data if data[i]<4] 
PassConditionB =  [i for i in data if data[i]%2 == 0]

print(PassConditionA) # output: [0, 1, 2, 3]
print(PassConditionB) # output: [0, 2, 4, 6, 8, 10]

PassJoinedConditions = list(set(PassConditionA) & set(PassConditionB))

print(PassJoinedConditions) # output: [0, 2]

print(data)
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

data = [data[i] for i in PassJoinedConditions]

print(data)
# output: [0, 2]

# found the would-be question answered here
# https://stackoverflow.com/questions/16028304/is-it-safe-to-assign-list-comprehension-to-the-original-list
