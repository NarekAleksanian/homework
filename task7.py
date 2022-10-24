arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

arr2 = [[10, 12, 13],
        [14, 15, 16],
        [17, 18, 19]]

arr3 = []


column = 0
column2 = 0
tmp = []

while column < len(arr) or column2 < len(arr2):
    row = len(arr[column]) - 1
    row2 = len(arr2[column]) - 1
    while row >= 0:
        tmp.append(arr[column][row])
        row -= 1
    while row2 >= 0:
        tmp.append(arr2[column2][row2])
        row2 -= 1
    arr3.append(tmp)
    tmp = []
    column += 1
    column2 += 1

print(arr3)


# for row, row2 in zip(arr, arr2):
#     tmp = []
#     for i, j in zip(row, row2):
#         tmp.append(i)
#         tmp.append(j)
#     arr3.append(tmp)

print(arr3)

