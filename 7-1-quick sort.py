# if you put array into function through param, array itself will rebuild (if dont want to, try use A.copy())
# better way than throwing back and forth


def quick_sort(A, s, e):
    if s >= e:
        return

    p = partition(A, s, e)
    quick_sort(A, s, p - 1)
    quick_sort(A, p + 1, e)


def partition(A, s, e):
    pivot = A[e]
    i = s - 1

    for j in range(s, e):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    i += 1
    A[i], A[e] = A[e], A[i]
    return i


A = [100, -13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -94]
quick_sort(A, 0, len(A) - 1)
print(A)
