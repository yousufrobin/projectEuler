import time

start_time = time.time()
extension = 1000
list = []
for i in range(1, extension+1):
	result = 1
	for j in range(i):
		result *= i
		
	list.append(result)

print(str(sum(list))[-10:])
end_time = time.time()
print(end_time-start_time)

# second method is way faster
start_time = time.time()
extension = 1000
solution = 0
for i in range(1, extension+1):
	solution += i**i

print(str(solution)[-10:])
end_time = time.time()
print(end_time-start_time)	