import re

def solution(s):
    p = re.compile(r'(\w)\1')
    while True:
        changed = p.sub('', s, count=1)
        if changed == '':
            return 1
        if changed == s:
            return 0
        s = changed

print(solution('baabaa'))