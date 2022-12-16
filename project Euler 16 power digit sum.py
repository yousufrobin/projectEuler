base = 2
power = 1000

result = 1

for i in range(1000):
	result *= base
print(result)


stringResult = str(result)
summation = 0
for i in range(len(stringResult)):
	summation += int(stringResult[i])
print(summation)
	