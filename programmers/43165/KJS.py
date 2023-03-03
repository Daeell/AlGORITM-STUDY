def solution(numbers, target):
    answer = 0
    parent = [0]
    leaves = []
    for i in range(len(numbers)):
        for j in range(len(parent)):
            leaves.append(parent[j]+numbers[i])
            leaves.append(parent[j]-numbers[i])
            # if i == len(numbers)-1:
            #     if parent[j]+numbers[i] == target or parent[j]-numbers[i] == target:
            #         answer +=1
        parent = []
        parent.extend(leaves)
        leaves = []
    # print(parent)
    for num in parent:
        if num == target:
            answer += 1
            
    
    return answer
