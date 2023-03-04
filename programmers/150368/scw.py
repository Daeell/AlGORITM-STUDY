from itertools import product

def solution(users, emoticons):

    answer = [0,0]

    discount = [40, 30, 20, 10]
    for sales in product(discount, repeat=len(emoticons)):
        max_money = 0
        subscribe = 0

        for rate, limit in users:
            user_money =0
            for i in range(len(emoticons)):
                if rate <= sales[i]:
                    user_money += int(emoticons[i] * ((100-sales[i])*0.01))

            if user_money >= limit:
                subscribe +=1
            else:
                max_money += user_money

        if subscribe > answer[0]:
            answer[0] = subscribe
            answer[1] = max_money
        elif subscribe == answer[0] and answer[1]< max_money:
            answer[1] = max_money
    
    return answer

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))