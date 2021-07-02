def gen_subsets(k):  # {0, 1, ..., n - 1} 집합의 모든 부분집합을 출력 부분집합의 개수가 2^n이므로 그 이상의 수행 시간 필요
    if(k == n):
        print(S)
    else:
        S.append(k)
        gen_subsets(k+1)
        S.pop()
        gen_subsets(k+1)


S = []
n = int(input())
gen_subsets(0)
