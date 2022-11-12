import sys
from collections import defaultdict
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

arr = []
dic = defaultdict(int)
total = 0
N= int(input())
for i in range(N):
    num = int(input())
    arr.append(num)
    total+= num
    dic[num]+=1


arr.sort()
print(round(total/N)) # 산술평균
print(arr[N//2]) # 중앙값
print(dic)
print(arr[N-1]-arr[0]) #범위


# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.