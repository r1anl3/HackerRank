#where is used as filter, where chỉ dùng để xét điều kiện, không tác động lên phần tử
from pipe import where, select, chain, traverse, groupby, dedup
arr = [1,2,3,4,5]
print( "Ket qua cua where = ",list(arr | where(lambda x : x % 2 == 0)))
#select is used as map, select dùng để tác động lên phần tử
print("Ket qua cua map = ", list(arr | select(lambda x : x * 2)))
#select + where: lọc phần tử rồi thực hiện lệnh
listt = list(arr
    | where(lambda x : x % 2 == 0)
    | select(lambda x : x * 2))
print("Ket qua cua where + select = ", listt)
#chain: gộp list in list (cấp 1)
nested = [[1,2,[3]], [5,6]]
print("Ket qua cua chain = ", list(nested | chain))
#traverse: đưa về 1 list
print("Ket qua cua traverse = ", list(nested | traverse))
#traverse + select lên dictionary
dict = [
    {"name" : "john", "age" : [18]},
    {"name" : "kevin", "age" : 19},
    {"name" : "kwan", "age" : 20}
]
rs = list(dict 
    | select(lambda x : x["age"])
    | traverse)
print("Ket qua cua select + traverse = ", rs)
#groupby: nhóm các phần tử theo điều kiện
# nếu chỉ dùng groupby, kết quả sẽ là "địa chỉ", nên dùng chung với select
data = (1,2,3,4,5,6,7,8,9) #tuple
gr = list(data
    | groupby(lambda x : "Even" if x % 2 == 0 else "Odd")
    | select(lambda x :  {x[0] : list(x[1])} )) # chuyển thành dictionary
a = gr
print("Ket qua cua groupby = ", gr)
#dedup: xóa phần tử trùng lặp trong mảng
data2 = [1,2,3,3,3,5,5,6,4,4]
data2.sort()
print("Ket qua cua dedup = ", list(data2 | dedup(lambda key : key < 5)))