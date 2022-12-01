import sys
input = sys.stdin.readline

def go():
    count = int(input())
    category = {}   # { 카테고리 : 해당 카테고리의 옷의 개수 }
    for _ in range(count):
        name_in, ctg_in = input().split()
        if ctg_in not in category:
            category[ctg_in] = 1
        else:
            category[ctg_in] += 1
    
    answer = 1
    for key in category:
        answer *= (category[key]+1)

    print(answer - 1)


TESTCASE = int(input())

for _ in range(TESTCASE):
    go()