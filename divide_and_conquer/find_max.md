- find_max1

  - T(n) = T(n - 1) + c, T(1) = 1
  - T(n) = O(n)

- find_max2

  - T(n) = 2\*T(n/2) + c, T(1) = 1
  - T(n) = O(n)

* 두 함수의 차이점은 선형 재귀 호출 vs 이진 재귀 호출
