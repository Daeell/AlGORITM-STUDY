from itertools import combinations
import sys
N, K = map(int, sys.stdin.readline().split())
answer = 0

default_word = {'a','n','i','c','t'}

remain_alphbet = set(chr(i) for i in range(97,123)) - default_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(N)]

def countwords(data,can_use):
    cnt = 0
    for word in data:
        can_read = 1
        for w in word:
            if can_use[ord(w)] == 0:
                can_read = 0
                break
        
        if can_read == 1:
            cnt += 1
    return cnt

if K >=5:
    # 아스키코드 사용하여 해당 알파벳의 사용 여부를 확인
    can_use = [0] * 123
    for x in default_word:
        can_use[ord(x)] = 1  # 무조건 배워야하는 알파벳 아스키코드 인덱스 value를 1로 최신화

    # default_alphabet 를 빼고 남은 모든 알파벳에서 K-5개를 선택하는 경우의수를 다 돌아보면서 answer를 최대값으로 최신화 시킨다
    for teach in list(combinations(remain_alphbet,K-5)):
        for t in teach:
            can_use[ord(t)] = 1
        cnt = countwords(data,can_use)

        if cnt > answer:
            answer = cnt
        for t in teach:
            can_use[ord(t)] = 0
    
    print(answer)
else:
    print(0)
