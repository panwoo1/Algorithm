# 가장 작은 수부터 차례대로 찾는 방식(큰 수부터 찾을 수도 있음)

def insertion_sort(A, n):
    for i in range(1, n):
        j = i - 1
        while(j >= 0 and A[j] > A[j+1]):
            A[j], A[j+1] = A[j+1], A[j]
            j = j - 1


A = [12, 4, 9, 10, 21, 3, 8, 0, 7, 9, 6]
insertion_sort(A, len(A))
print(A)
