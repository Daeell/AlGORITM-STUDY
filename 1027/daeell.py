import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline


def solution():
    # 가장 많은 고층빌딩이 보이는 고층빌딩을 찾는다.
    # 빌딩은 N개가 있다.
    # 빌딩은 (순서, 높이)의 선분으로 나타낸다.
    n = int(input())
    heights = list(map(int, input().split()))
    left = [0]*n
    right = [0]*n

    left[0] = 1
    for i in range(1, n):
        left[i] = 1
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                if left[i] < left[j] + 1:
                    left[i] = left[j] + 1

    right[n-1] = 1
    for i in range(n-2, -1, -1):
        right[i] = 1
        for j in range(i+1, n):
            if heights[i] < heights[j]:
                if right[i] < right[j] + 1:
                    right[i] = right[j] + 1

    answer = 0
    for i in range(n):
        if answer < left[i] + right[i] - 1:
            print(i)
            answer = left[i] + right[i] - 1

    return answer


print(solution())
