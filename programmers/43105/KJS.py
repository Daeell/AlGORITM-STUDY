def solution(triangle):
    answer = 0
    num = []
    length = len(triangle)
    for i in range(length):
        num.append([0]*(i+1))
    num[0][0] = triangle[0][0]
    # 점화식?
    # num[i][j] = triangle[i][j] + max(num[i-1][j-1], num[i-1][j]) - j == 0, j == len(num[i]) -1  다르게
    for i in range(1,length):
        for j in range(i+1):
            if j == 0:
                num[i][j] = num[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                num[i][j] = num[i-1][j-1] + triangle[i][j]
            else:
                num[i][j] = triangle[i][j] + max(num[i-1][j-1], num[i-1][j])
                
    answer = max(num[length-1])
    return answer
