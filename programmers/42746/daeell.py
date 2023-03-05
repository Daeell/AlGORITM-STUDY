def solution(numbers):
    numbers = list(map(str, numbers))

    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)

    answer = ''.join(numbers)
    return answer if int(answer) != 0 else "0"


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

# 시간초과
# def solution(numbers):
#     # 1. 문자열로 변환
#     numbers = list(map(str, numbers))

#     # 2. 두 문자열을 합쳐 비교하는 함수
#     def compare(a, b):
#         return int(a+b) > int(b+a)

#     # 3. 선택 정렬을 이용한 정렬
#     for i in range(len(numbers)):
#         max_idx = i
#         for j in range(i+1, len(numbers)):
#             if compare(numbers[j], numbers[max_idx]):
#                 max_idx = j
#         numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

#     # 4. 최종 결과를 문자열로 반환
#     answer = ''.join(numbers)
#     return answer if int(answer) != 0 else "0"
