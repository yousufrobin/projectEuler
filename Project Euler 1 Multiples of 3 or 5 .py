num_array = []
three_array = []
five_array = []

three_multi = 0
five_multi = 0

while three_multi < 1000:
    num_array.append(three_multi)
    three_array.append(three_multi)
    three_multi += 3


while five_multi < 1000:
    if five_multi not in num_array:
        num_array.append(five_multi)
    five_multi += 5

total = 0
for j in num_array:
    total = total + j
print(total)
