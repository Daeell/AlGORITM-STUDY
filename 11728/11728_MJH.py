A_LEN, B_LEN = map(int, input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
arr = []

def append_while_small_than_n (which_list, idx, n):
    while idx < len(which_list):
        if A[idx] <= n:
            arr.append(A[idx])
            idx += 1
        else:
            break
    return idx

a_idx = 0
b_idx = 0
if A[0] < B[0]:
    a_idx = append_while_small_than_n (A, a_idx, B[b_idx])
    b_idx = append_while_small_than_n (B, b_idx, A[a_idx])