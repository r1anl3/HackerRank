#code mượn 
from collections import deque #tạo block phân chia vùng, tránh tràn data

with open('D:\Python\day6.txt', 'r') as f:
    data = [int(i) for i in f.read().split(',')]

def AOC_day6_pt2(days):
    totals = deque(data.count(i) for i in range(9)) # đếm số lượng các số từ 0 -> 8 có trong data
    for _ in range(days):
        totals.rotate(-1)#dịch sang trái 1 đơn vị/ tức sau mỗi ngày sẽ giảm mỗi số 1 đơn vị. Khi về số 0, sẽ đẩy sang số 8
        totals[6] += totals[8] # qualtity(số 6) += qualtity(số 8)
    return sum(totals)
print(AOC_day6_pt2(256))
