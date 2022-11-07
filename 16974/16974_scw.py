import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

N, X =map(int,input().strip().split())

burger=[1]*51 # 버거 최대 레벨 공간
patty=[1]*51 # 패티 최대 레벨 공간

for i in range(1, N+1): # 미리 각 레벨 마다 burger의 개수와 patty의 개수를 구해놓음
    burger[i] = 3 + burger[i-1]*2
    patty[i] = patty[i-1]*2 + 1


def solve(n, x): # 패티 개수를 구하자
    if n==0: # 레벨 0이면 둘중하나 처음부터 0이었거나 재귀를 타서 내려왔거나
        return x # 이러면 먹은 개수를 그냥 돌려보내주면됨
    if x==1: # 여기 걸린다는건 level은 남았지만 먹은게 1이라는거 그래서 빵만 먹음
        return 0 # 빵만 먹음
    elif x <=1 + burger[n-1]: # 먹은게 중간보다 아래면
        return solve(n-1,x-1) # n==0일때까지 계속 쪼개면서 내려감
    elif x == 1 + burger[n-1] +1: # 먹은게 딱 중간까지 이면
        return patty[n-1] +1 # 아까 구한 patty 개수 + 1개 해주면됨
    elif x<=burger[n-1]*2 +2: # 먹은게 중간보다 크고 끝까지 보단 작으면
        return patty[n-1] + 1 + solve(n-1, x-burger[n-1]-2) # 이전 패티양 + 중간 패티 + 남은 길이에서 패티 찾기 --> x - burger[n-1]-2 = 먹은 양 - 이전 level의 버거 개수 - 현재 레밸에서 더해진 버거 2개 = 이전 레벨에서의 먹은 위치
    else: # 끝까지 다먹었으면
        return patty[n] #patty 값 반환

print(solve(N,X))
