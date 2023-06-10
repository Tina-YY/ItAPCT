# count inversions - official solution


def count_inversions(A, p, r):
    inversions = 0
    if p < r:
        q = int((p + r) / 2)
        inversions = inversions + count_inversions(A, p, q)
        inversions = inversions + count_inversions(A, q + 1, r)
        inversions = inversions + merge_inversions(A, p, q, r)
    return inversions


def merge_inversions(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L, R = [], []
    for i in range(0, n1):
        L.append(A[p + i])
    for j in range(0, n2):
        R.append(A[q + j + 1])

    L.append(999999)
    R.append(999999)

    i = 0
    j = 0
    inversions = 0
    counted = False
    for k in range(p, r + 1):
        if counted is False and R[j] < L[i]:
            inversions = inversions + n1 - i
            counted = True
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
            counted = False

    return inversions


A_ = [2, 3, 8, 6, 1]
in_ = count_inversions(A_, 0, len(A_) - 1)
print(in_)
print(A_)
