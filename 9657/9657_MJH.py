def DFS(current_rock) -> int:
    if DP[current_rock] != -1:
        return DP[current_rock]
    for i in range(3):
        win_probability = 0
        n = DFS(current_rock - pick_rock[i])
        if n != 0:
            win_probability = 1
            DP[current_rock] = n
    if win_probability == 0:
        DP[current_rock] = 0

N = int(input())
DP = [-1]*(1001)
DP[1] = 1
DP[2] = 0
DP[3] = 3
DP[4] = 4
pick_rock = (1, 3, 4)
if DFS(N) == 0:
    print("CY")
else: print("SK")