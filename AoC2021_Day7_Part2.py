#đọc dữ liệu
with open("D:\Python\day7.txt", 'r') as f:
    data = [int(i) for i in f.read().split(',')]
    star, end = min(data), max(data) + 1
#tính sigma
def sigma(a,b):
    n = abs(a - b)
    return (n*(n+1))//2
#function chính
def aoc_part2():
    cost = []
    for i in range(star, end):
        cost.append(sum(sigma(i, pos) for pos in data))
    return cost
print(aoc_part2())