# 가장 큰 값 부터 차례대로 찾는 방식(작은 수부터 찾을 수 있음)

def bubble_sort(A, n):
    for i in range(n):
        for j in range(1, n):
            if(A[j-1] > A[j]):
                A[j-1], A[j] = A[j], A[j-1]


A = [12, 4, 9, 10, 21, 3, 8, 0, 7, 9, 6]
bubble_sort(A, len(A))
print(A)
