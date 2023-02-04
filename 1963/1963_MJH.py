import sys
from collections import deque
input = sys.stdin.readline

def do_prime() -> list:
    arr = [0 for _ in range(10000)]
    for i in range(2, 10000):
        if arr[i] == 0:
            n = 2
            mul = i*n
            while mul < 10000:
                arr[mul] = 1
                n += 1
                mul = i*n
    return arr


def detect(src:str, dst:str) -> int:
    queue = deque()
    queue.append((src, 0))
    visited = set()
    while queue:
        src, cnt = queue.popleft()
        if src == dst:
            break
        visited.add(src)
        for i in range(4):
            if src[i] == dst[i]:
                continue
            for n in range(10):
                tmp = list(src)
                tmp[i] = str(n)
                tmp = ''.join(tmp)
                if tmp[0] == str(0):
                    continue
                if tmp not in visited and PRIME[int(tmp)] == 0:
                    queue.append((tmp, cnt+1))

    return cnt


PRIME = do_prime() # PRIME[i] == 0 이면 소수

for _ in range(int(input().strip())):
    a, b = input().split()
    print(detect(a, b))