def get_max_index(A, i):
    max_index = 0
    for j in range(i+1):
        if(A[j] > A[max_index]):
            max_index = j
    return max_index

# 가장 큰 값부터 차례대로 찾는 방식(작은 수부터 찾을 수 있음)


def selection_sort(A, n):
    for i in range(n-1, 0, -1):
        # get_max_index(A, i)는 A[0], ..., A[i] 중 최대값의 배열 인덱스를 리턴하는 함수
        m = get_max_index(A, i)
        # A[m]이 현재 최대값이므로 A[i]에 배치되어야 함.  따라서 A[i]와 A[m]을 자리바꿈(swap)
        A[i], A[m] = A[m], A[i]


A = [12, 4, 9, 10, 21, 3, 8, 0, 7, 9, 6]
selection_sort(A, len(A))
print(A)
