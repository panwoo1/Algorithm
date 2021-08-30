import random, timeit

def quick_sort(A, first, last):  # in-place-2
    if(first >= last):
        return
    smaller, equal, larger = first, first, last + 1
    pivot = A[first]

    while(equal < larger):
        if(A[equal] < pivot):
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif(A[equal] == pivot):
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

    quick_sort(A, first, smaller - 1)
    quick_sort(A, smaller + 1, last)


def merge_sort(A, first, last):
    if(first >= last):
        return
    middle = (first + last) // 2
    merge_sort(A, first, middle)
    merge_sort(A, middle + 1, last)
    B = []
    i = first
    j = middle + 1
    while(i <= middle and j <= last):
        if(A[i] <= A[j]):
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    for i in range(i, middle + 1):
        B.append(A[i])
    for j in range(j, last + 1):
        B.append(A[j])
    for k in range(first, last + 1):
        A[k] = B[k-first]


def heap_sort(A):
    global Hc, Hs
    # make heap
    n = len(A)
    for i in range(n//2, -1, -1):
        c, s = heapify_down(A, i, n)
        Hc += c
        Hs += s
    # sort
    for i in range(n-1, 0, -1):
        Hs += 1
        A[0], A[i] = A[i], A[0]
        n = n - 1
        c, s = heapify_down(A, 0, n)
        Hc += c
        Hs += s


def heapify_down(A, k, n):
    comp, swap = 0, 0
    while 2*k+1 < n:
        L, R = 2*k + 1, 2*k + 2
        comp += 2
        if A[L] > A[k]:
            m = L
        else:
            m = k
        if R < n and A[R] > A[m]:
            m = R
        if m != k:
            A[k], A[m] = A[m], A[k]
            k = m
            swap += 1
        else:
            break
    return comp, swap
