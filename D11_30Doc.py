arr = []
def hourglass(list):
	hg = []
	for i in range(4):
		for j in range(4):
			sum = list[i][j] + list[i][j+1] + list[i][j+2] + list[i+1][j+1] + list[i+2][j] + list[i+2][j+1] + list[i+2][j+2]
			hg.append(sum)
	return hg
		

for _ in range(6):
	arr.append(list(map(int, input().rstrip().split())))
print(hourglass(arr))