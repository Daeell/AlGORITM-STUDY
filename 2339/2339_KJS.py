import sys
N = int(sys.stdin.readline())
stoneBoard = []
for _ in range(N):
    stoneBoard.append(list(map(int, sys.stdin.readline().split())))

print(stoneBoard)

# 1. 불순물(1)을 포함하고 있는 지점으로 자르며, 가로 또는 세로로 자를 수 있다.
# 2. 석판을 자를 때 이전에 자른 방향과 같은 방향으로 자를 수 없다.
#    (그림을 보면 어떠한 말을 하는지 알 것)
# 3. 결정체가 있는 곳은 자를 수 없다.
# 4. 결정체끼리 붙어있으면 무조건 자를 수 없다 => res = -1

