import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().split())
        building_time_data = list(map(int, sys.stdin.readline().split()))
        building_time_data.insert(0, 0)
        order_graph = [[] for _ in range(N+1)]
        in_degree = [0 for _ in range(N+1)]
        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            order_graph[X].append(Y)
            in_degree[Y] += 1
        W = int(sys.stdin.readline())
        dp = [0 for _ in range(N+1)]
        queue = []
        for i in range(1, N+1):
            if in_degree[i] == 0:
                queue.append(i)
                dp[i] = building_time_data[i]
        while queue:
            now = queue.pop(0)
            for i in order_graph[now]:
                in_degree[i] -= 1
                dp[i] = max(dp[i], dp[now] + building_time_data[i])
                if in_degree[i] == 0:
                    queue.append(i)
        print(dp[W])

main()