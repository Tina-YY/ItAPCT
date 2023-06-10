# find maximum sub-array


def find_maximum_subarray(A, start, end):
    if end - start <= 1:
        if A[start] >= A[end]:
            return start, start + 1, A[start]
        else:
            return end, end + 1, A[end]

    mid = int((end + start) / 2)
    L_start, L_end, L_max = find_maximum_subarray(A, start, mid)            # 找左侧
    R_start, R_end, R_max = find_maximum_subarray(A, mid + 1, end)        # 找右侧
    M_start, M_end, M_max = find_across_maximum_subarray(A, start, end)     # 从中间开始向两侧找
    if L_max >= R_max and L_max >= M_max:
        return L_start, L_end, L_max
    if R_max >= L_max and R_max >= M_max:
        return R_start, R_end, R_max
    return M_start, M_end, M_max


def find_across_maximum_subarray(A, start, end):
    mid = int((end - start) / 2)
    L_max, R_max = 0, 0
    L_sum, R_sum = 0, 0
    L_pos, R_pos = mid, mid

    for i in range(mid, end + 1):
        R_sum += A[i]
        if R_sum > R_max:
            R_max = R_sum
            R_pos = i + 1               # 如果这里是i，那最后给出的答案就是包括右侧index[start, end]，现在是[start, end)，这里用i+1是为了区分没有最优的情况
    for i in range(mid - 1, start - 1, -1):
        L_sum += A[i]
        if L_sum > L_max:
            L_max = L_sum
            L_pos = i

    return L_pos, R_pos, R_max + L_max


# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# A = [13, -3, 25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# A = [-1, -2, -3]
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 100]
# A = [100, -13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -94]
l, r, m = find_maximum_subarray(A, 0, len(A) - 1)
print(l, r, m)


# 关键步骤是从中间开始向两侧找的那部，所有max subarray最开始诞生的地方都在这个子步骤里
