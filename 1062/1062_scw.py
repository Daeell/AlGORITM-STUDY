#가르침
import sys
from itertools import combinations
input=sys.stdin.readline

n, k = map(int, input().strip().split())

answer = -1
if k>=5:
    remain_words = list()
    remain_words_for_comb= list()
    for _ in range(n):
        a = set(input().strip())-{'a','n','c','t','i'}
        if a == None:
            continue
        remain_words.append(a)
        for i in range(len(a)):
            if list(a)[i] not in remain_words_for_comb:
                remain_words_for_comb.append(list(a)[i])
    
    if k-5 > len(remain_words_for_comb):
        print(n)
        exit(0)

    for comb in combinations(remain_words_for_comb, k-5):
        comb_set = set(comb)
        cnt = 0
        for word in remain_words:
            if word.issubset(comb_set):
                cnt+=1
        answer=max(answer,cnt)

    
    print(answer)
else:
    print(0)

    
        


# #가르침 -- 시간초과
# import sys, re, copy
# from itertools import combinations
# input=sys.stdin.readline

# n, k = map(int, input().strip().split())

# words_2=[]
# for i in range(n):
#     a=list(set(re.sub(r"[a,n,t,i,c]","",(sys.stdin.readline().strip()))))
#     if a ==[]:
#         continue
#     words_2.append(a)

# if k<5:
#     print(0)
# elif k==5:
#     print(n-len(words_2))
# else:
#     test_list=set()

#     for i in range(len(words_2)):
#         for j in words_2[i]:
#             test_list.add(j)

#     answer_real=0
#     if len(test_list) < k-5:
#         k = len(test_list) +5

#     for i in combinations(test_list, k-5):
#         words = copy.deepcopy(words_2)
#         answer = 0
#         alp=[0]*26
#         for a in i:
#             alp[ord(a)-97]=1

#         for q in words:
#             temp = len(q)
#             for w in range (temp):
#                 if(str(type(q[w])) == "<class 'str'>"):
#                     if alp[ord(q[w])-97]== 1:
#                         q[w]=1
#             cnt=0
#             for c in range(len(q)):
#                 if q[c] == 1:
#                     cnt+=1
#             if cnt == len(q):
#                 answer+=1
            
#         answer_real= max(answer_real,answer)
#     answer_real += n-len(words_2)
#     print(answer_real)
