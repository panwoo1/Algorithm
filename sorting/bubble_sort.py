def bubble_sort(A, n):
    for i in range(n):
        for j in range(1, n):
            if(A[j-1] > A[j]):
                A[j-1], A[j] = A[j], A[j-1]


A = [3, 1, 2, 4]
bubble_sort(A, len(A)-1)
print(A)
