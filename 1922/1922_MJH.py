import sys
input = sys.stdin.readline

def main():
    NUMBER_OF_MACHINES = int(input().strip())
    NUMBER_OF_LINES = int(input().strip())
    line_info = []
    for _ in range(NUMBER_OF_LINES):
        line_info.append(list(map(int, input().split())))

    parent_info = [-1 for _ in range(NUMBER_OF_MACHINES + 1)]  # UNUSED index '0'
    line_info.sort(key=lambda x: x[2])

    def find_root(cur):
        while parent_info[cur] != cur:
            cur = parent_info[cur]
        return cur

    total_cost = 0
    connection_count = 0
    for i in range(NUMBER_OF_LINES):
        # 종료조건: N-1개의 라인이 연결되면 종료합니다.
        if connection_count == NUMBER_OF_MACHINES - 1:
            break

        # 조건에 따라 간선을 연결하고 연결정보(부모)를 업데이트합니다.
        a = line_info[i][0]  # Machine 'A'
        b = line_info[i][1]  # Machine 'B'
        cost = line_info[i][2]
        if a == b:
            continue
        elif parent_info[a] == -1 and parent_info[b] == -1:
            parent_info[a] = a
            parent_info[b] = a
        elif parent_info[a] == -1:
            parent_info[a] = find_root(b)
        elif parent_info[b] == -1:
            parent_info[b] = find_root(a)
        else:
            a_root = find_root(a)
            b_root = find_root(b)
            if a_root == b_root:
                continue
            parent_info[a_root] = parent_info[b_root]

        # 비용을 더해주고 개수를 카운트합니다.
        total_cost += cost
        connection_count += 1

    print(total_cost)


main()