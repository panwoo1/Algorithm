def find_max(A, n):
    if(n == 1):
        return A[0]
    return max(find_max(A, n-1), A[-1])


A = [1, 3, 2, 4]
print(find_max(A, len(A)-1))
