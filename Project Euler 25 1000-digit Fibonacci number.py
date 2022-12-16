num1 = 1
num2 = 2
num3 = num1 + num2

fib = [1,2]
while len(str(num3)) < 1000:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    fib.append(num3)
    
print(len(fib) + 1)
		