def gen_permutation():  # 길이가 n인 모든 순열을 출력 순열의 개수가 n! 이므로 그 이상의 시간이 필요
    if(len(P) == n):
        print(P)
    else:
        for i in range(1, n+1):
            if(chosen[i] == True):
                continue
            chosen[i] = True
            P.append(i)
            gen_permutation()
            chosen[i] = False
            P.pop()


P = []
n = int(input())
chosen = [False for _ in range(n+1)]
gen_permutation()
