n = int(input())
_list = []
cnt = 0
for _ in range(n) :
    _list.append(input().rstrip())

    
# 문자열 크기 차이가 2이상이면 continue 시키는건 맞음
norm_word = _list[0]
# print(norm_word)

norm_dict = dict()
for alphabet in norm_word :
    if alphabet in norm_dict :
        norm_dict[alphabet] += 1
    else :
        norm_dict[alphabet] = 1

# print(norm_dict)

for word in _list[1:] :
    if abs(len(word) - len(norm_word)) > 2 :
        continue
    
    check_dict = norm_dict.copy()
    res = 0

    for val in word :
        if val in check_dict and check_dict[val] != 0 :
            check_dict[val] -= 1
        else :
            res += 1

    if sum(check_dict.values()) < 2 and res < 2 :
        cnt += 1

print(cnt)

    
