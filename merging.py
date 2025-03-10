arr1 = [1, 1, 2, 3, 5, 8, 13, 21]
arr2 = [2, 3, 5, 7, 11, 13, 17, 19]
arr3: list[int] = []

i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

while i < len(arr1):
    arr3.append(arr1[i])
    i += 1

while j < len(arr2):
    arr3.append(arr2[j])
    j += 1

print(arr3)

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
