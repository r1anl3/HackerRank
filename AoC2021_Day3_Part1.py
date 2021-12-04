bit = []
#tạo input
while True:
    n = str(input())
    if 'c' in n:
        break
    bit.append(n)
#tạo list đếm số lượng bit
list_0 = []
list_1 = []
#đếm bit theo cột
for i in range(len(bit[0])):
    #tạo biến đếm bit
    count_0 = 0
    count_1 = 0
    for j in range(len(bit)):
        if bit[j][i] == '1':
            count_1 += 1
        if bit[j][i] == '0':
            count_0 += 1
    #thêm biến đếm vào bit
    list_0.append(count_0)
    list_1.append(count_1)
#tạo list chứa bit
result_1 = []
result_2 = []
for i in range(len(bit[0])):
    if list_0[i] > list_1[i]:
        result_1.append('0')
        result_2.append('1')
    else:
        result_1.append('1')
        result_2.append('0')
#convert bit từ string sang initial
for i in range(len(result_1)):
    result_1[i] = int(result_1[i])
    result_2[i] = int(result_2[i])
#biến đổi bit sang decimal
def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))
#tạo biến gamma, epsilon
gamma = binatodeci(result_1)
epsilon = binatodeci(result_2)
print(gamma * epsilon)
