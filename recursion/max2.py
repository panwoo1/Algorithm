def find_greater(x, y):
    if (x > y):
        return x
    else:
        return y

def max2(A):
    if(len(A) == 1):
        return A[0]
    return find_greater(max2(A[:len(A)//2]), max2(A[len(A)//2:]))
