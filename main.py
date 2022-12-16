x = [
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7]
]

col_num = 7
row_num = 5
multi_time = 4

multiple = 1
multiples = []
for i in range(0,row_num-3): # row
    for j in range(0,col_num-3): #col
        for k in range(0,4):
            multiple *= x[k+i][i+k]
        multiples.append(multiple)
        print(multiple)
        multiple = 1








# # diagonally left to right,downward
# multiple = 1
# multiples = []
#
# for i in range(0,row_num-3): # row
#     for j in range(0,col_num-3): #col
#         for k in range(0,4):
#             multiple *= x[i+k][j+k]
#         multiples.append(multiple)
#         print(multiple)
#         multiple = 1
#
#
# # up to down straight
# multiple = 1
# multiples = []
# for i in range(0, col_num):
#     for j in range(0, row_num - 3):
#         for k in range(0, multi_time):
#             multiple *= x[j + k][i]
#         multiples.append(multiple)
#         print(multiple)
#         multiple = 1
#
# # left to right straight
# multiple = 1
# multiples = []
#
# for i in range(0, col_num - 3):
#     for j in range(0, row_num):
#         for k in range(0, multi_time):
#             multiple *= x[j][k + i]
#         multiples.append(multiple)
#         print(multiple)
#         multiple = 1
