from collections import Counter #đếm số
data = open("day5.txt").read().strip().split("\n")# mở file.đọc.cắt space đầu cuối.xuống dòng
segment = [] # list tọa độ
for line in data:
    x1, y1 = tuple(int(x) for x in line.split(" -> ")[0].split(","))
    #for x in line.split(' -> ')[0] : line bị chia cắt bởi ' -> ', bên trái là [0] bên phải là [1]
    #.split(',') : giá trị bị chia cắt bởi ',' , x1 = giá trị bên trái x2 = giá trị bên phải
    x2, y2 = tuple(int(x) for x in line.split(" -> ")[1].split(","))
    if x1 == x2 or y1 == y2: #nếu hoành != hoành hoặc tung != tung thì không thể nằm trên 1 đường thẳng
        for x in range(min(x1,x2), max(x1,x2) + 1):
            for y in range(min(y1,y2), max(y1,y2) + 1):
                segment.append((x,y))
part1 = 0
for count in Counter(segment).values():
# Counter(segment) : đếm giá trị giống nhau trong segment, trả về (segment) : value
    if count > 1:
        part1 += 1
print(part1)
