from collections import deque
with open("D:\Python\day7.txt", 'r') as f:
    data = [int(i) for i in f.read().split(',')]
horizon = deque(data)
fuel = []
def aoc_part1(list, n):
    cost = 0
    for i in range(len(list)):
        if list[i] != n:
            cost += abs(n - list[i])
    return cost
for i in range(len(horizon)):
    fuel.append(aoc_part1(horizon, horizon[i]))
print(min(fuel))
