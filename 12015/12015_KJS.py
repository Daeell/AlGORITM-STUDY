# import sys
# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))

# dp = [1] * N

# for i in range(N):
#     for j in range(0,i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(dp)



import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
emul_A = list(enumerate(A))
emul_A = sorted(emul_A, key = lambda x : (x[1], x[0]))
print(emul_A)
# A_sort = sorted(A)
