factorial = 100
result = factorial

for i in range(factorial-1,0,-1):
    result *= i

factorial_result = str(result)
sum = 0
for i in factorial_result:
    sum += int(i)

print(sum)