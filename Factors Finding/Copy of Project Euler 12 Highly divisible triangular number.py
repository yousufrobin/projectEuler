import math


def factors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors += 2
        else:
            continue
    return number_of_factors


triangle_num = 1
for i in range(2, 1000000):
    triangle_num += i
    if factors(triangle_num) >= 500:
        print(triangle_num)
        break
