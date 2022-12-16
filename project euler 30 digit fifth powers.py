import time

start_first = time.time()
result = 0
for i in range(2, 5*9**5+1):
	if sum([int(x)**5 for x in str(i)]) == i:
		result += i
		
end_first = time.time()		
print(result)
print(end_first - start_first)

# elaboration of - if sum([int(x)**5 for x in str(i)]) == i: first method takes less time
start_time = time.time()
result = 0
for i in range(2, 5*9**5+1):
	tempo_result = 0
	for x in str(i):
		tempo_result += int(x)**5
	if tempo_result == i:
		result += i

end_time = time.time()		
print(result)
print(end_time - start_time)	