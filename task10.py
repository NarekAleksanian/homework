arr = [1, 6, 7, 5, 2, 3]

for i in range(int(len(arr)/2)):
    if arr[i] % 2 != 0:
        for j in range(len(arr)-1, -1, -1):
            if arr[j] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
                break

print(arr)

lowest = arr[0]
lowest2 = arr[0]

for i in arr:
    if i < lowest:
        lowest = i


# task 7

for i in arr:
    if i % 2 == 0:
        print(i)


# task 8
for i in arr:
    if i % 2 != 0:
        print(i)


# task 9
tmp = []

for i in arr:
    if i % 2 != 0:
        tmp.append(i)

print(tmp)

task 11

arr23 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

arr24 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def matrix(arr1, arr2):
    for row, row2 in zip(arr1, arr2):
        for elem1, elem2 in zip(row, row2):
            if elem1 != elem2:
                return False
    return True


print(matrix(arr23, arr24))
