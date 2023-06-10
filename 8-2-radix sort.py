# can only deal with positive numbers
import math


def radix_sort(A):
    maxA = max(A)
    digit = int(math.log(maxA, 10) + 1)

    base = 10
    for i in range(digit):
        A = counting_sort(A, base)
        base *= 10

    return A


# default: decimal, so array_size = 10
def counting_sort(A, base):
    C = []
    for i in range(10):
        C.append(0)

    _A = A.copy()
    B = A.copy()
    B.append(0)

    for i in range(len(A)):
        _A[i] = int((_A[i] % base) / (base / 10))
        C[_A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        B[C[_A[i]]] = A[i]
        C[_A[i]] -= 1

    A = B[1:]
    return A


A_ = [100, 13, 3, 25, 20, 3, 16, 23, 18, 20, 7, 12, 5, 22, 15, 94]
A_ = radix_sort(A_)
print(A_)
