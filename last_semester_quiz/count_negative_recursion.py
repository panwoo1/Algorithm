def count_negative(L, a, b):
	count = 0
	if(a == b):
		if(L[a] < 0):
			return 1
		return 0
	if(L[a] < 0):
		count += 1
	m = (a + b) // 2
	return count_negative(L, a, m) + count_negative(L, m+1, b)
	
	
# 리스트 L 입력 받음
L = list(map(int, input().split()))
print(count_negative(L, 0, len(L)-1))