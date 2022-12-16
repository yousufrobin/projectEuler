extension = 100
list = []
for num in range(2, extension+1):
	result = num
	for i in range(0, extension-1):
		result *= num
		list.append(result)

listt = []
for j in list:
	if j not in listt:
		listt.append(j)
		
print(listt)
print(len(listt))