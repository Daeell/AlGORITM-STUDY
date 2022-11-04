import sys
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
scores = []
for i in range(N):
    scores.append(int(input()))

criterion = scores[-1]
ans = 0 
for i in range(N-2, -1, -1):
    if scores[i] >= criterion : 
        ans += (scores[i]- (criterion-1)) 
        scores[i] = criterion-1
    criterion = scores[i]

print(ans)
