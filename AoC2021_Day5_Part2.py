from collections import Counter
data = open("day5.txt").read().strip().split("\n")
segment = []
for line in data:
    x1, y1 = tuple(int(x) for x in line.split(" -> ")[0].split(","))
    x2, y2 = tuple(int(x) for x in line.split(" -> ")[1].split(","))
    if x1 == x2 or y1 == y2:
        for x in range(min(x1,x2), max(x1,x2) + 1):
            for y in range(min(y1,y2), max(y1,y2) + 1):
                segment.append((x,y))
    else:
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + step_x, step_x):
            segment.append((x,y))
            y += step_y
part2 = 0
for count in Counter(segment).values():
    if count > 1:
        part2 += 1
print(part2)
