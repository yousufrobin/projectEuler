import math

amicable_num = []
x = list(range(1, 10001))
for num in x:
    number = num
    factors_sum = 0
    for i in range(1, math.floor(number/2)+1):
        if number % i == 0:
            factors_sum += i

    factors_sum_second = 0
    for second in range(1, math.floor(factors_sum/2) + 1):
        if factors_sum % second == 0:
            factors_sum_second += second

    if factors_sum != factors_sum_second:
        if num == factors_sum_second:
            amicable_num.append(factors_sum)
            amicable_num.append(factors_sum_second)

print(amicable_num)

amicable_num_sum = 0
for i in amicable_num:
    amicable_num_sum += i


summation = int(amicable_num_sum / 2)

print(summation)