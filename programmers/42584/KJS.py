from collections import deque
def solution(prices):
    prices_q = deque(prices)
    # print(prices_q)
    answer=[]
    
    while prices_q:
        price = prices_q.popleft()
        
        sec = 0
        for next_price in prices_q:
            if price > next_price:
                sec +=1
                break
            sec += 1
        
        answer.append(sec)
    
    
    return answer
