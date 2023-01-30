import re
import collections


def solution(s):
    answer = list()
    numbers = re.findall(r'\d+', s)
    numbers_count = collections.Counter(numbers)
    numbers_count = sorted(numbers_count.items(),
                           key=lambda x: x[1], reverse=True)
    for number, count in numbers_count:
        answer.append(int(number))
    return answer
