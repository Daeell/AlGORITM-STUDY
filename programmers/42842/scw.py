
def solution(brown, yellow):
    answer = []
    
    yaksu=[]
    def find_yaksu(num):
        i=1
        while (i*i<=num):
            if num%(i)==0:
                yaksu.append(num//(i))
            i+=1

    def find_carpet(yaksu, brown, answer):
        
        for i in yaksu:
            width = i
            height = yellow//i
            if (width+2)*2 + height*2 == brown:
                answer.append(width+2)
                answer.append(height+2)
                break
        return answer

    
    find_yaksu(yellow)
    find_carpet(yaksu, brown, answer)
    # print(yaksu)

    return answer


print(solution(8, 1))