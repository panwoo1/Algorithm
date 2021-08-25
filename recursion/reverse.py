def reverse_1(A):
    if(len(A) == 1):
        return A
    return reverse_1(A[1:]) + A[:1]


def reverse_2(A, start, stop):
    if(start < stop - 1):
        A[start], A[stop - 1] = A[stop - 1], A[start]
        reverse_2(A, start + 1, stop - 1)

def reverse_3(A, a):
    n = len(A)
    if a < n // 2:
        A[a], A[n-a-1] = A[n-a-1], A[a]
        reverse_3(A, a+1)

A = [1, 2, 3, 4, 5, 6, ]

A = reverse_1(A)
print(A)
reverse_2(A, 0, len(A))
print(A)
reverse_3(A, 0)
print(A)
