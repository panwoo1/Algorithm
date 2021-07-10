def power2(a, n):  # 이중 재귀 호출로 작성하기
    if(n == 0):
        return 1
    if(n % 2 == 1):
        return power2(a, n//2)*power2(a, n//2)*a
    else:
        return power2(a, n//2)*power2(a, n//2)


def fibonacci1(n):
    if(n <= 1):
        return n
    return fibonacci1(n-1) + fibonacci1(n-2)


def fibonacci2(n):
    pass


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
print(fibonacci1(n), fibonacci2(n), fibonacci3(n), fibonacci4(n), fibonacci5(n))
