n, x = map(int, input().split())
visit = list(map(int, input().split()))

_max = sum(visit[:x])
_sum = _max
cnt = 1

for i in range(n-x) :
    _sum += visit[x+i] - visit[i] 

    if _max == _sum :
        cnt += 1
    elif _max < _sum :
        cnt = 1
        _max = max(_max, _sum )

if _max == 0 :
    print("SAD")
else :
    print(_max, cnt, sep='\n')

