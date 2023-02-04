import sys

# num의 노드를 삭제할때 사용하는 함수
def dfs(num,arr):
    # 인풋으로 받은 arr에서 num 째 수를 -2로 바꾸어주면서 삭제가 되었다고 표기해두기
    arr[num] = -2
    for i in range(len(arr)):       # arr의 리스트를 순회하면서 num같은 리스트가 있다고 하면 dfs()를 실행
        if num == arr[i]:
            dfs(i,arr)

N = int(sys.stdin.readline())
root_input = list(map(int, sys.stdin.readline().split()))
select = int(sys.stdin.readline())


dfs(select,root_input)
count = 0
# print(root_input)
for i in range(len(root_input)):
    # 입력받은 리스트에서 -2로 되었다는 것은 삭제되었고,
    # 그리고 i가 리스트에 없다는 것은 i를 부모로 두는 리프노드가 없는 것으로 판별하기에
    # count를 진행해준다
    if root_input[i] != -2  and i not in root_input:
        # print(i)
        count += 1

print(count)
