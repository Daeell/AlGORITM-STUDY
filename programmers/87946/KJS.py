def solution(k, dungeons):
    answer = -1
    dungeons.sort(key = lambda x:(-x[0], x[1]))
    cnt = 0
    graph = [0] * len(dungeons)
    a = k
    # for i in range(len(dungeons)):
    #     if k >= dungeons[i][0] and graph[i] ==0:
    #         for j in range(i+1,len(dungeons)):
    #             if k-dungeons[j][1] >= dungeons[i][0] and graph[j] ==0 :
    #                 k -= dungeons[j][1]
    #                 graph[j] = 1
    #                 cnt +=1
    #         if k >= dungeons[i][0] and graph[i] == 0:
    #             k -= dungeons[i][1]
    #             graph[i] = 1
    #             cnt += 1
    def find(a,arr,cnt,graph):  
        for i in range(len(arr)):
            if a >= arr[i][0] and graph[i] ==0:
                for j in range(i+1,len(arr)):
                    if a-arr[j][1] >= arr[i][0] and graph[j] ==0 :
                        a -= arr[j][1]
                        graph[j] = 1
                        cnt +=1
                if a >= arr[i][0] and graph[i] == 0:
                    a -= arr[i][1]
                    graph[i] = 1
                    cnt += 1
        return cnt
    for i in range(len(graph)):
        cnt += find(a,dungeons,cnt,graph)
    
    answer += cnt
    
            
    
    return answer
