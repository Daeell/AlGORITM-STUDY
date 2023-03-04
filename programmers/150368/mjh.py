# 정답입니다!
from itertools import product
def solution(users, emoticons):
    total_signed = 0
    total_sales = 0
    
    discount_rate = [40, 30, 20, 10]
    rates = list(product(discount_rate, repeat = len(emoticons)))
    
    for i in range(len(rates)):
        emoticon_prices = [emoticons[j]-(emoticons[j]//100)*rates[i][j] for j in range(len(rates[0]))]
        signed = 0
        sales = 0
        
        for user in users:
            rate, limit = user
            purchased = 0
            for j in range(len(emoticon_prices)):
                if rate <= rates[i][j]:
                    purchased += emoticon_prices[j]
            if purchased >= limit:
                signed += 1
            else:
                sales += purchased
                
        if signed > total_signed:
            total_signed = signed
            total_sales = sales
        elif signed == total_signed and sales > total_sales:
            total_sales = sales
                
    return [total_signed, total_sales]