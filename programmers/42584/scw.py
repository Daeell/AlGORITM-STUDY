def solution(prices):
    answer = []
    min_stock = 10001
    cnt =0
    temp = []
    while prices:
        stock = prices.pop()

        if stock <= min_stock:
            answer.append(cnt)
            min_stock = stock            
        else:
            for i in range(len(temp)-1,-1,-1):
                if stock >temp[i]:
                    answer.append(len(temp)-i)
                    break

        temp.append(stock)
        cnt+=1

    answer.reverse()

    return answer

print(solution([1, 2, 3, 2, 3, 1]))