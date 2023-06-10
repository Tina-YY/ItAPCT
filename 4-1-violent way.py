# find maximum sub-array


def find_maximum_subarray(A):
    answer = 0
    right, left = 0, 0
    for i in range(len(A)):
        temp_sum = 0
        for j in range(i, len(A)):
            temp_sum += A[j]
            if temp_sum > answer:
                right, left = i, j + 1
                answer = temp_sum
    return right, left, answer


# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# A = [13, -3, 25, 20, -3, -16, -23, 18, 20, -7, 10, -5, -22, 15, -4, 7]
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -94, 100]
# A = [-1, -2, -3]
l, r, m = find_maximum_subarray(A)
print(l, r, m)
