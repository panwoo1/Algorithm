#최대 구간 합 계산
#수행시간 O(n)

def max_interval(A, n):
	S = [0] * len(A)
	S[0] = A[0]
	
	for k in range(1, n):
		S[k] = max(S[k-1] + A[k], A[k])
		
	return max(S)

n = int(input())
A = [int(x) for x in input().split()]
print(max_interval(A, n))