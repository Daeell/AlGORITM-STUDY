def solution(n, info):
    answer = []
    
    def find_max(n):
        temp=10
        s=0
        maxi=0
        while(s<n):
            maxi +=temp
            s +=1
            temp -=1
        return maxi
    
    maxi=find_max(n)

    apeach_score =0
    for i in range(len(info)):
        if info[i] !=0:
            apeach_score +=(10-i)
    
    if maxi == apeach_score:
        answer.append(-1)
        return answer
    


    print(maxi)
            

    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))