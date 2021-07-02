def factorial(n):
    if(n == 1):
        return n
    else:
        return n * factorial(n - 1)


# Tail Recursion ... recursion stack의 내용을 overwrite하는 식으로 메모리 사용을 크게 줄일 수 있다.
def tail_factorial(n, value=1):
    if(n == 1):
        return value
    else:
        return tail_factorial(n-1, value * n)


# 호출과정
'''
tail_factorial(4)
tail_factorial(3, 1*4)   #value = 1
tail_factorial(2, 4*3)   #value = 4
tail_factorial(1, 12*2)  #value = 12
tail_factorial(1)        #value = 24
'''
