divRange = 21
def check(num):
	for i in range(11, divRange):
		if num % i == 0:
			continue
		else:
			return False
	return True


num = 2520
while not check(num):
	num += 20
print(num)