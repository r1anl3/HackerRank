depth = []
while True:
    try:
        depth.append(int(input()))
    except:
        break

count = 0
for i in range(len(depth)-1):
    if depth[i] < depth[i+1]:
        count += 1
print(count)