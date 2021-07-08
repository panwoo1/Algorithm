def power1(a, n):  # 선형 재귀 호출로 작성하기
    if(n == 1):
        return a
    return a * power1(a, n-1)


def power2(a, n):  # 이중 재귀 호출로 작성하기
    if(n == 0):
        return 1
    if(n % 2 == 1):
        return power2(a, n//2)*power2(a, n//2)*a
    else:
        return power2(a, n//2)*power2(a, n//2)


def power3(a, n):
    if(n == 0):
        return 1
    p = power3(a, n // 2)
    if(n % 2 == 1):
        return p * p * a
    else:
        return p * p

# pow(x, y) x^y를 계산
# y가 음수일 수도 있음!


def pow(x, y):
    if(y < 0):
        y = abs(y)
        return power3(1/x, y)
    return power3(x, y)


a, n = 2, 4
print(power1(a, n), power2(a, n), power3(a, n))
print(pow(a, n))
print(pow(2, -4))
