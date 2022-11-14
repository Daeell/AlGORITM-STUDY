import sys
input = sys.stdin.readline
N = int(input())
input_arr = list(map(int, input().split()))
# 인풋받은것을 정렬한다. (원래 인덱스 값을 가지고 있어야 함)
# 제일 작은 수부터 시작해서 0부터 시작하는 번호를 붙인다.
# 만일 같은 수(중복)이면 번호는 증가하지 않는다.
for i in range(N):
    tmp = input_arr[i]
    input_arr[i] = [tmp, i]  # index정보를 가지고 있기 위해서 묶어줌

sorted_arr = sorted(input_arr)

tmp = sorted_arr[0][0]  # 이전 값 저장을 위한 변수
compressed_idx = 0      # 압축 좌표는 0에서 시작한다.
for i in range(N):
    if sorted_arr[i][0] == tmp:
        input_arr[sorted_arr[i][1]].append(compressed_idx)
    else:
        tmp = sorted_arr[i][0]
        compressed_idx += 1
        input_arr[sorted_arr[i][1]].append(compressed_idx)

for i in range(N):
    print(input_arr[i][2], end=' ')