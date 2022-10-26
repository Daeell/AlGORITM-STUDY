import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
list_ = []
for _ in range(n):
    word = input().rstrip()
    list_.append(word)

sorted_list = list(sorted(list_))
# 단어를 알파벳 순으로 정렬한다.
cnt = []

for i in sorted_list:
    cnt.append(list_.count(i))
# 정렬한 인덱스를 순회하면서 각 인덱스의 단어가 몇 개가 있는지 세준다.

print(sorted_list[cnt.index(max(cnt))])
# max를 하게되면 같은 값이면 가장 앞에 나온게 해당되므로 해당 인덱스를 가진 것을 출력하면 된다.
