# PASSED
def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    stk = []

    for i in range(len(prices)):
        while stk:
            price, idx = stk[-1]
            if price > prices[i]:
                answer[idx] = i - idx
                stk.pop()
            else:
                break
        stk.append((prices[i], i))
        
    return answer