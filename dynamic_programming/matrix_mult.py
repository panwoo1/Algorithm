# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

#행렬곱셈 문제
#수행시간 O(n^3)
def matrix_mult():
    for x in range(1, n):
    	for i in range(n-x):
            j = i + x
            C[i][j] = math.inf # math module에서 제공하는 매우 큰 정수
            for k in range(i, j):
                cost = min(C[i][j], C[i][k] + C[k+1][j] + P[i-1]*P[k]*P[j])
                if C[i][j] > cost:
                    C[i][j] = cost
    return C[0][-1]

n = int(input()) # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in input().split()] # M_i = p_i x p_{i+1}
C = [[0]*n for _ in range(n)] # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult()
print(min_cost)