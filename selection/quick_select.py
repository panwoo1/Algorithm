def Quick_Select(L, k):
    A, M, B = [], [], []
    p = L[0]
    for a in L:
        if(a < p):
            A.append(a)
        elif(a == p):
            M.append(a)
        else:
            B.append(a)
    if(len(A) >= k):
        return Quick_Select(A, k)
    elif(len(A) + len(M) < k):
        return Quick_Select(B, k - len(A) - len(M))
    else:
        return p
