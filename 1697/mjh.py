from collections import deque
def main():
    start_point, end_point = map(int, input().split())

    if start_point >= end_point:
        return start_point - end_point

    queue = deque()
    visited = set()
    queue.append((start_point, 0))
    visited.add(start_point)
    while queue:
        position, time = queue.popleft()
        if position == end_point:
            return time
        if position*2 < end_point*2 and position*2 not in visited:
            visited.add(position*2)
            queue.append((position*2, time+1))
        if position+1 not in visited:
            visited.add(position+1)
            queue.append((position+1, time+1))
        if position-1 not in visited:
            visited.add(position-1)
            queue.append((position-1, time+1))

print(main())