import numpy as np

list2d = []

with open('D:\Python\day9.txt', 'r') as f:
    for line in f.readlines():
        list2d.append(list(line.rstrip('\n')))

array2d = np.array(list2d).astype(np.int32)
# arr_mask = np.full(np.shape(array2d), -1)
max_y, max_x = np.shape(array2d)

total = 0
for y in range(max_y):
    for x in range(max_x):
        debug_value = array2d[y][x]
        count = 0
        if x != 0:
            if array2d[y][x] < array2d[y][x-1]:
                count += 1
        else:
            count += 1
        if x != max_x-1:
            if array2d[y][x] < array2d[y][x+1]:
                count += 1
        else:
            count += 1
        if y != 0:
            if array2d[y][x] < array2d[y-1][x]:
                count += 1
        else:
            count += 1
        if y != max_y-1:
            if array2d[y][x] < array2d[y+1][x]:
                count += 1
        else:
            count += 1
        if count == 4:
            # arr_mask[y][x] = array2d[y][x]
            total += array2d[y][x] + 1

print(total)