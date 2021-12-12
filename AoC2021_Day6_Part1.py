data = open("D:\Python\day6.txt").read().strip().split(",")
for i in range(len(data)):
    data[i] = int(data[i])
for day in range(80):
    for i in range(len(data)):
        if data[i] == 0:
            data.append(8)
            data[i] = 6
        else:
            data[i] -= 1
print(len(data))
