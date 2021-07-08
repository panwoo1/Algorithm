def find_max1(A):
    if(len(A) == 1):
        return A[0]
    else:
        return max(A[0], find_max1(A[1:]))


def find_max2(A):
    if(len(A) < 1):
        return -float('inf')
    elif(len(A) == 1):
        return A[0]
    else:
        return find_max2(max(A[:len(A)//2], A[len(A)//2:]))


A = [1, 2, 3, 4, 5]
print(find_max1(A), find_max2(A))
