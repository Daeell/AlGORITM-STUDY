# PASSED
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        min_l = min(len(phone_book[i-1]), len(phone_book[i]))
        if phone_book[i-1][:min_l] == phone_book[i][:min_l]:
            answer = False
            break
    return answer

print(solution(["119", "97674223", "1195524421"]))