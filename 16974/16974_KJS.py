import sys
sys.setrecursionlimit(10**6)

N,X = map(int,sys.stdin.readline().split())
buger = [[] for _ in range(N+1)]
buger[0] = 'P'
buger[1] = 'BPPPB'
# print(buger)
# def makeBuger(N):
#     if N ==0:
#         buger[N] = 'P'
#     elif N == 1:
#         buger[N] = 'B' + buger[0] + 'P' + buger[0] + 'B'
#     else:
#         buger[N] = 'B' + makeBuger(N-1) + 'P' + makeBuger(N-1) + 'B'

# makeBuger(N)
# print(buger)
def bugermake(N,X):
    for i in range(2,N+1):
        buger[i] = 'B' + buger[i-1] + 'P' + buger[i-1] + 'B'

    bugerList = list(buger[N])
    cnt = 0
    for i in range(X):
        if bugerList[i] == 'P':
            cnt +=1
        else:
            continue
    print(cnt)
bugermake(N,X)




