# right up diagonals
right_up_diagonals = []
for i in range(1, 1002, 2):
    right_up = i*i
    right_up_diagonals.append(right_up)
right_up_diagonals.pop(0)

# right down diagonals
right_down_diagonals = []
x = 6
for j in right_up_diagonals:
    right_down = j - x
    right_down_diagonals.append(right_down)
    x += 6

# left down diagonals
left_down_diagonals = []
y = 2
for k in right_down_diagonals:
    lef_down = k + y
    left_down_diagonals.append(lef_down)
    y += 2

# left up diagonals
left_up_diagonals = []
z = 2
for l in right_up_diagonals:
    left_up = l - z
    left_up_diagonals.append(left_up)
    z += 2

right_left_down = right_up_diagonals
right_left_down.extend(left_down_diagonals)
right_left_down.append(1)

left_right_down = left_up_diagonals
left_right_down.extend(right_down_diagonals)

all = right_left_down
all.extend(left_right_down)

# print(all)

result = 0
for m in all:
    result +=m

print(result)