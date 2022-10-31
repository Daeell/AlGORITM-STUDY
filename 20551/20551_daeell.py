import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def b_search(target):
    left = 0
    right = len(a_arr)-1
    while left <= right:
        mid = (left+right)//2
        if a_arr[mid] > target:
            right = mid-1
        elif a_arr[mid] < target:
            left = mid+1
        elif a_arr[mid] == target:
            if a_arr[right] == mid:
                break
            right = mid
    if a_arr[mid] == target:
        return mid
    else:
        return -1

# while left < right:
#     mid = left + (right - left) // 2
#     if a_arr[mid] < target:
#         left = mid + 1
#     else:
#         right = mid

# return right


n, m = map(int, input().split())

a_arr = [int(input()) for _ in range(m)]
m_arr = [int(input()) for _ in range(m)]
a_arr.sort()


for target in m_arr:
    print(b_search(target))
