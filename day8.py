from collections import deque
#đọc file
with open('D:\Python\day8.txt', 'r') as f:
    data = deque(f.read().strip().split('\n'))
#lọc data
digits = []
output = []
for lines in data:
    digits.append([str(i) for i in lines.split(' | ')[1].split(' ')])
for i in digits:
    for j in i:
        output.append(j)
#function chính
def aoc_part1(list):
    result = 0
    display = [2, 3, 4, 7] # 2: '1', 3: '7', 4:'4' , 7:'8'
    for n in list:
        if len(n) in display:#so sánh độ dài n trong list với display để tìm ra số 1, 4, 7, 8
            result += 1
    return result
print(aoc_part1(output))