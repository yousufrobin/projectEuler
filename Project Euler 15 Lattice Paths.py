import time
# I very happy to solve this problem using Dynamic Programming technique
# by myself with the help of Allah.
x_axis_or_column = int(input("Please insert the number of column: "))
y_axis_or_row = int(input("Please insert the number of row: "))

start_time = time.time()

root_list = list(range(3,y_axis_or_row+2))

for i in range(3, x_axis_or_column + 2):
    result_list = root_list
    result = i
    temp_result_list = []

    for j in result_list:
        result += j
        temp_result_list.append(result)

    root_list = list(temp_result_list)
    temp_result_list.clear()

end_time = time.time()
total_time = end_time-start_time
print(f'the number of routes through {x_axis_or_column}X{y_axis_or_row} grid is {root_list[-1]}')
print(f'it took {total_time} seconds to solve the problem')