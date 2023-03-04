# 안~풀려요~
def binary_stringify(num):
    s = str(format(num, 'b'))
    if len(s)%2 == 0:
        s = '0'+s
    return s

def check_BT(s):
    def checker(left, right):
        mid = (left+right)//2
        if s[mid] == '0':
            return False
        if right - left <= 2:
            return True
        if checker(left, mid-1) and checker(mid+1, right):
            return True
        return False
    return 1 if checker(0, len(s)-1) else 0

def solution(numbers):
    answer = []

    for num in numbers:
        print(binary_stringify(num))
        answer.append(check_BT(binary_stringify(num)))

    return answer

print(solution([15]))