# time complexity: O(n)
# no negative ones


def counting_sort(A):
    maxA = max(A)
    # init
    C = []
    for i in range(maxA + 1):
        C.append(0)
    # counting
    for i in A:
        C[i] += 1
    # counting less
    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]

    B = A.copy()
    B.append(0)
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1

    return B[1:]


# A_ = [2, 3, 8, 6, 1]
A_ = [13, 3, 25, 20, 3, 16, 23, 18, 20, 7, 10, 5, 22, 15, 4, 7]
B_ = counting_sort(A_)
print(B_)
