def sum(n):
    if(n <= 1):
        return n
    return n + sum(n-1)


def sum(a, b):
    if(a > b):
        return 0
    if (a == b):
        return a
    m = (a + b) // 2
    return sum(a, m) + sum(m + 1, b)
