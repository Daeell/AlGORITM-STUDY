k = 80	
dun= [[80,20],[50,40],[30,10]]

def howMany(i, dungeons) : 



def solution(k, dungeons):
# 현재 피로도보다 최소 필요도가 높은 곳은 아예 제낌
# 현재 피로도에서 각각을 순회하면서 소모 필요도를 썼을 때
# 갈 수 있는 곳이 가장 많은 곳들이 후보로 남게됨 
# 각각에 대해 재귀로 확인 

    #각각의 요소를 순회하면서, 갈 수 있는 곳 중, 이 곳을 간다면 그 다음으로 갈 수 있는 곳의 갯수를 얻어서 compare 배열에 넣는다
    compare = []
    for i in range(len(dungeons)) :
        howMany(i, dungeons)
    
    #compare 값이 가장 높은 곳을 선택했을 때, 


    
    answer = -1
    return answer

print(solution(k, dun))
