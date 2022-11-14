import sys
sys.stdin= open("input.txt", "r")
input= sys.stdin.readline
N = int(input())


# 검색해서 가져온 quick_sort 코드 (아래) 써도 시간초과는 마찬가지
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array
    pivot, tail = array[0], array[1:]
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

origin_arr = list(map(int, input().split()))
sorted_arr = quick_sort((list(set(origin_arr))))
table = dict()
for item in origin_arr :
    val = table.get(item)
    if val != None :
        ans = val
    else: 
        ans = sorted_arr.index(item)
        table[item]= ans 
    print(ans, end =" ")



