def power2(a, n):  # 이중 재귀 호출로 작성하기
    if(n == 0):
        return 1
    if(n % 2 == 1):
        return power2(a, n//2)*power2(a, n//2)*a
    else:
        return power2(a, n//2)*power2(a, n//2)

def calculate_matrix(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]

    return C


def fibonacci1(n):
    if(n <= 1):
        return n
    return fibonacci1(n-1) + fibonacci1(n-2)


def fibonacci2(A, n):
    
    if(n > 1):
        A = fibonacci2(A, n//2)
        A = calculate_matrix(A, A)

        if(n % 2 == 1):
            F1 = [[1, 1], [1, 0]]
            A = calculate_matrix(A, F1)

    return A



def fibonacci3(n):
    if(n == 0 or n == 1):
        return n
    k = n//2
    Fk = fibonacci3(k)
    Fk_minus_1 = fibonacci3(k-1)
    Fk_plus_1 = Fk_minus_1 + Fk

    if(n % 2 == 0):
        return Fk*Fk + 2*Fk*Fk_minus_1
    else:
        return Fk_plus_1 * Fk_plus_1 + Fk * Fk


def fibonacci4(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return F[n]


def fibonacci5(n):
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b


n = int(input())
A = [[1, 1], [1, 0]]
A = fibonacci2(A, n)
print(fibonacci1(n), fibonacci3(n), fibonacci4(n), fibonacci5(n))
print(A[0][1])