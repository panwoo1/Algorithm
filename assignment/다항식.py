import time, random

def evaluate_n2(A, x):
	# code for O(n^2)-time function
	result = 0
	for i in range(1, len(A)): #1차항 부터 n차항 까지 계산
		order = 1
		order *= A[i]
		for j in range(i):
			order *= x
		result += order
	result += A[0] #0차항 
	return result
	
def evaluate_n(A, x):
	# code for O(n)-time function
	result = 0
	for i in range(len(A)-1, 0, -1):	#다항식을 a0 + x(a1 + x(a2+...+x(an+0)))
		result += A[i]
		result *= x
	result += A[0]
	return result
	
random.seed()		# random 함수 초기화
n = int(input())# n 입력받음
A = [random.randint(-1000,1000) for _ in range(n)]# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
x = random.randint(-1000, 1000)
start1 = time.process_time()
a = evaluate_n2(A, x)# evaluate_n2 호출
end1 = time.process_time()
start2 = time.process_time()
b = evaluate_n(A, x)# evaluate_n 호출
end2 = time.process_time()
print("evalute_n^2의 결과", a)
print()
print("evalute_n^2의 수행시간", end1 - start1)# 두 함수의 수행시간 출력
print()
print("evalute_n의 결과", b)
print()
print("evalute_n의 수행시간", end2 - start2)