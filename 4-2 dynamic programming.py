# find maximum sub-array


def find_maximum_subarray(A):
    subSum, tmpMax = 0, 0
    left = 0
    maxL, maxR = 0, 0
    for i in range(len(A)):
        subSum += A[i]
        if subSum > tmpMax:
            tmpMax = subSum
            maxL, maxR = left, i + 1
            continue

        if subSum < 0:
            subSum = 0
            left = i + 1

    return maxL, maxR, tmpMax


# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# A = [13, -3, 25, 20, -3, -16, -23, 18, 20, -7, 10, -5, -22, 15, -4, 7]
# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -94, 100]
A = [100, -13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -94, 100]
# A = [-1, -2, -3]
l, r, m = find_maximum_subarray(A)
print(l, r, m)
