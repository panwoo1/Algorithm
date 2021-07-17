def insertion_sort(A, n):
    for i in range(1, n):
        j = i - 1
        while(j >= 0 and A[j] > A[j+1]):
            A[j], A[j+1] = A[j+1], A[j]
            j = j - 1


A = [3, 1, 2, 4]
insertion_sort(A, len(A)-1)
print(A)
