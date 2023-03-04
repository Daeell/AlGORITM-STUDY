
def solution(dirs):
    answer = 0
    # 좌표는 가로 세로 -5 ~ 5, 출발은 (0,0)
    #예외처리
    #1. 좌표를 벗어나는 경우
    #2. 방문한 길인 경우 
    directions = {"U": (0,1), "D": (0,-1), "L":(-1,0), "R":(1,0)}
    visited= set()
    robot = [0,0]
    for i in dirs : 
        tmpX= robot[0]+ directions[i][0]
        tmpY = robot[1]+ directions[i][1]

        if tmpX< -5 or tmpX>5 or tmpY <-5 or tmpY>5 : 
            continue 
            
        # 이전 위치와 현재 위치를 string으로 road로 표시
        road = str(robot) + str([tmpX, tmpY])

        roadReverse= str([tmpX, tmpY]) + str(robot)

        # 위치 갱신
        robot[0]= tmpX
        robot[1]= tmpY
        
        if road not in visited : 
            visited.add(road)
            visited.add(roadReverse)

            answer +=1 
        
    
    return answer

print(solution("ULURRDLLU"))  #7
