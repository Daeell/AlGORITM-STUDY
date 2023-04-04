def isGroup(word) :
    not_series = []

    for _alphabet in word :
        if not not_series :
            not_series.append(_alphabet)
        
        if not_series[-1] != _alphabet :
            not_series.append(_alphabet)

    
    check_set = set()
    for alphabet in not_series :
        if alphabet in check_set :
            return False
        else :
            check_set.add(alphabet)
            
    return True

n = int(input())
res = 0
for i in range(n) :
    word = input().strip()
    if isGroup(word) == True :
        res += 1

print(res)
