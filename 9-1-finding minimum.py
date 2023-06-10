def minimum(A):
    x = 999999
    for i in A:
        if i < x:
            x = i
    return x


def minimum_and_maximum(A):
    lengthA = len(A)
    maxA, minA = None, None
    if lengthA % 2 == 1:
        maxA, minA = A[0]
        A = A[1:]
    else:
        maxA, maxB = A[0], A[1]
        A = A[2:]

    # 3 times of comparison for each one pair
    for i in range(len(A) - 1):
        bigger, smaller = A[i], A[i + 1]
        if A[i] < A[i + 1]:
            bigger, smaller = smaller, bigger
        maxA = max(maxA, bigger)
        minA = min(minA, smaller)

    return maxA, minA
