import random


def quick_sort_1(A, first, last):  # in-place-1
    if (first >= last):
        return
    left, right = first + 1, last
    pivot = A[first]
    while (left <= right):
        while(left <= last and A[left] < pivot):
            left += 1
        while(right > first and A[right] >= pivot):
            right -= 1
        if(left <= right):
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

    A[first], A[right] = A[right], A[first]
    quick_sort_1(A, first, right - 1)
    quick_sort_1(A, right + 1, last)


def quick_sort_2(A, first, last):  # in-place-2
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

    quick_sort_2(A, first, smaller - 1)
    quick_sort_2(A, smaller + 1, last)


def quick_sort_3(A):  # not-in-place
    if(len(A) <= 1):
        return A
    pivot = A[0]
    S, M, L = [], [], []
    for x in A:
        if(x < pivot):
            S.append(x)
        elif(x > pivot):
            L.append(x)
        else:
            M.append(x)
    return quick_sort_3(S) + M + quick_sort_3(L)


def print_list(quick_sort):
    print(A)
    quick_sort(A, 0, len(A)-1)
    print(A)


A = [4, 2, 5, 8, 6, 2, 3, 7, 10]

# print_list(quick_sort_1)
# print_list(quick_sort_2)
# print(quick_sort_3(A))
