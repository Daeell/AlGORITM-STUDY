# def solution(want, number, discount):
#     answer = 0
#     product_to_id = {product: i for i, product in enumerate(want)}
#     discount_date = [[]for _ in range(len(want))]
#     for date, id_ in enumerate(discount):
#         if id_ in product_to_id:
#             discount_date[product_to_id[id_]].append(date)

#     for i in range(len(discount)):
#         available_discounts = []
#         for j, product in enumerate(want):
#             if len(discount_date[j]) > 0 and i <= discount_date[j][-1] and i+9 <= discount_date[j][-1]:
#                 available_discounts.append(product_to_id[product])
#         if len(available_discounts) == len(want) and len(set(discount_date[k][-1] for k in available_discounts)) == 1:
#             return i + 1
#     return answer

from bisect import bisect_left


def solution(want, number, discount):
    wants = []
    for w, n in zip(want, number):
        wants += [w] * n
    wants.sort()

    for i in range(len(discount) - len(wants) + 1):
        if wants[0] not in discount[i:]:
            continue

        j = bisect_left(discount, wants[0], i)
        if sorted(discount[j:j+len(wants)]) == wants:
            return i + 1

    return 0


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
      "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
