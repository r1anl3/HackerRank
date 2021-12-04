bit = []
#tạo input
while True:
    n = str(input())
    if 'c' in n:
        break
    bit.append(n)
#tìm bit xuất hiện nhiều nhất
def get_MCV(b,d):
    ones_count = 0
    zeroes_count = 0
    for item in d:
        if item[b] == '1':
            ones_count += 1
        else:
            zeroes_count += 1

    if ones_count >= zeroes_count:
        return '1'
    else:
        return '0'
#tìm bit xuat hiện ít nhất
def get_LCV(b,d): 
    ones_count = 0 
    zeroes_count = 0 
    for item in d: 
        if item[b] == '1': 
            ones_count += 1 
        else: 
            zeroes_count += 1

    if ones_count < zeroes_count:
        return '1'
    else:
        return '0'
def perform_removals(b,d,m): #b: vị trí i của bit[i], d: bit list, m: bit xuất hiện ít/nhiều nhất
    removals_list = [] #list loại bỏ phần tử
    for item in d: 
        if item[b] != m: #nếu item thứ b (bit [i]) của d (bit list) khác m
            removals_list.append(item) #thêm vào list bỏ

    for removal in removals_list: #phần tử trong list bỏ
        bit.remove(removal) #bỏ phần tử trong list bỏ mà pt đó có trong bit

    return bit
bit2 = bit.copy() #tạo bản copy của bit để reset
for i in range(len(bit[0])):
    mcv = get_MCV(i, bit)
    bit = perform_removals(i, bit, mcv)
    if len(bit) == 1:
        oxygen_gen_rating = int(bit[0], 2)#?
        break
bit = bit2.copy() #reset lại bit list, dùng lại bit liat cũ
for i in range(len(bit[0])):
    lcv = get_LCV(i, bit)
    bit = perform_removals(i, bit, lcv)
    if len(bit) == 1:
        CO2_scrubber_rating = int(bit[0],2) #?
print(CO2_scrubber_rating * oxygen_gen_rating)