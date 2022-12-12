num = 13
b_num = bin(num)

print(f"Number is {num}")
print(num, b_num)
print()

print("trimming to just the numbers")
trim_b_num = b_num[2:]
print(trim_b_num)
print()

index_where_on = [i for i in range(len(trim_b_num)) if trim_b_num[i] == "1"]
print(index_where_on)
print()

messages = { 0 : "i want to be ",
             1 : "famous on TV ",
             2 : "up on the big screen",
             3 : "so you can hear me ",
             4 : "all you'll hear ",
             5 : "is my song in your head "}

for index in index_where_on:
  print(messages[index])

