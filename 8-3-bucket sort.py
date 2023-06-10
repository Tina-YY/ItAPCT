def bucket_sort(A, bucket_size=3):
    maxA = max(A)
    minA = min(A)

    bucket_number = int((maxA - minA) / bucket_size) + 1

    bucketArray = []
    for i in range(bucket_number):
        bucketArray.append([])

    for i in range(len(A)):
        position = int((A[i] - minA) / bucket_size)
        put_element_in_bucket(bucketArray, A[i], position)

    B = []
    for b in bucketArray:
        B += b

    return B


def put_element_in_bucket(B, number, position):
    B[position].append(number)
    for i in range(len(B[position]) - 1, 0, -1):
        if B[position][i] < B[position][i - 1]:
            B[position][i], B[position][i - 1] = B[position][i - 1], B[position][i]


A_ = [100, 13, 3, 25, 20, 3, 16, 23, 18, 20, 7, 12, 5, 22, 15, 94]
A_ = bucket_sort(A_)
print(A_)
