motion = []
step = []

while True:
    n = list(input().split())    
    if 'exit' in n:
        break
    motion.append(n[0])
    step.append(n[1])

horizontal_positon = 0
depth = 0
for i in range(len(motion)):
    if motion[i] == 'forward':
        horizontal_positon += int(step[i])
    if motion[i] == 'down':
        depth += int(step[i])
    if motion[i] == 'up':
        depth -= int(step[i])
print(horizontal_positon * depth)
