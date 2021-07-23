class Heap:

  def __init__(self, L=[]):
    self.A = L
    self.make_heap()
  
  def __str__(self):
    return str(self.A)

  def insert(self, key):
    self.A.append(key)
    self.heapfy_up(len(self.A)-1)

  def heapify_down(self, k, n):
    while(2*k + 1 < n):
      L, R = 2*k + 1, 2*k + 2
      if(L < n and self.A[L] > self.A[k]):
        m = L
      else:
        m = k
      if(R < n and self.A[R] > self.A[m]):
        m = R
      
      if(m != k):
        self.A[k], self.A[m] = self.A[m], self.A[k]
        k = m
      else:
        break

  def heapify_up(self, k):
    while(k > 0 and self.A[(k-1)//2] < self.A[k]):
      self.A[k], self.A[(k-1)//2] = self.A[(k-1)/2], self.A[k]
      k = (k-1)//2
    
  def make_heap(self):
    n = len(self.A)
    for k in range(n-1, -1, -1):
      self.heapify_down(k, n)

  def heap_sort(self):
    n = len(self.A)
    for k in range(len(self.A)-1, -1, -1):
      self.A[0], self.A[k] = self.A[k], self.A[0]
      n = n - 1
      self.heapify_down(0, n)

H = Heap([2,8,6,1,10,15,3,12,11])
print(H)
H.heap_sort()
print(H)