# 둘의 인덱스 차이가 2이하인 경우에 비교
# 거리두기가 아닌 경우?
# 2이하 인데 둘 사이에 X가 없다면 거리두기 안함


def solution(places):
    answer = []
    place = [list(places[0][i]) for i in range(len(places[0]))]
    p_index = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                p_index.append([i,j])
    print(p_index)
    for r,c in p_index:
        for r1,c1 in p_index:
            dist = abs(r-r1) + abs(c-c1)
            if 0< dist <=2:
                if dist ==1:
                    return 0
                elif r == r1 and place[r][min(c,c1)+1] == 'O':
                    return 0
                elif c == c1 and place[min(r,r1)+1][c] == 'O':
                    return 0
                elif 
    return answer

    
