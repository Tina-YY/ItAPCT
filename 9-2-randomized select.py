# start position; end position, target-th smallest number
def randomized_select(A, start, end, target):
    if start >= end:
        return A[start]

    k = partition(A, start, end)
    if k == target:
        return A[k - 1]
    if k < target:
        return randomized_select(A, k, end, target)
    else:
        return randomized_select(A, start, k - 2, target)


def partition(A, start, end):
    pivot = A[end]
    i = start - 1

    for j in range(start, end):
        if pivot > A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 2


# sorted:[3, 3, 5, 7, 12, 13, 15, 16, 18, 20, 20, 22, 23, 25, 94, 100]
A_ = [100, 13, 3, 25, 20, 3, 16, 23, 18, 20, 7, 12, 5, 22, 15, 94]
for i in range(1, len(A_) + 1):
    answer = randomized_select(A_, 0, len(A_) - 1, i)
    print(answer)
