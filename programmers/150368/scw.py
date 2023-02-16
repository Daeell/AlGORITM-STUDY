from itertools import permutations

def solution(users, emoticons):

    def dfs(x,y,depth):
        if depth ==3:
            return
        else:
            
        
    temp=[]
    for i in range(len(users)):
        temp.append(users[i][0])

    j =min(temp)

    if j <= 10:
        j =0
    elif j%10 ==0:
        j = j//10 -1
    else:
        j = j//10

    emoticons_sale = [[[10*i, emoticons[k]] for i in range(4,j,-1)] for k in range(len(emoticons))]


    for i in emoticons_sale:
        print(i)
    
    answer = []
    return answer

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))