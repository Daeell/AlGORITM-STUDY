from collections import Counter


def solution(want, number, discount):
    answer = 0
    buy_items = {}
    for w, n in zip(want, number):
        buy_items[w] = n
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == buy_items:
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
      "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
