depth = []
while True:
    try:
        depth.append(int(input()))
    except:
        break

count = 0
sum_count = []
for i in range(len(depth)-2):
    sum = depth[i] + depth[i+1] + depth[i+2]
    sum_count.append(sum)
for i in range(len(sum_count)-1):
    if sum_count[i] < sum_count[i+1]:
        count += 1
print(count)
