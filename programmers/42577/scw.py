#전화번호 목록

from collections import deque

def solution(phone_book):
    answer = True
    phone_book.sort()
    pb = deque(phone_book)
    forword = pb.popleft()
    while pb:
        if forword == pb[0][:len(forword)]:
            answer = False
            break
        forword = pb.popleft()
    
    return answer

print(solution(["123", "456", "789"]))