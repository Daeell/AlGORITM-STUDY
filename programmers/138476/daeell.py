import collections


def solution(k, tangerine):
    answer = 0
    tangerine_count = collections.Counter(tangerine)
    tangerine_count = sorted(tangerine_count.items(),
                             key=lambda x: x[1], reverse=True)
    for tangerine, count in tangerine_count:
        k -= count
        answer += 1
        if k <= 0:
            return answer

# 오답
#     answer = 0

#     set_list = list(set(tangerine))
#     count_list= list()

#     for i in range(len(set_list)):
#         count_list.append(tangerine.count(set_list[i]))
#     count_list.sort(reverse=True)

#     for j in range(len(count_list)):
#         k -= count_list[j]
#         answer += 1
#         if k <= 0:
#             return answer
