def solution(arrayA, arrayB):
    answer = 0
    
    def wantKnow(arr):
        data = []
        for i in range(2,arr[0]+1):
            for j in range(len(arr)):
                if j == len(arr)-1:
                    break
                if (arr[j] % i == 0) & (arr[j+1] % i == 0):
                    if i not in data:
                        data.append(i)
        return data
    
    
    def findMaxNum(arrA,arrB):
        num = 1
        for i in arrA:
            ans = []
            for j in range(len(arrB)):
                if arrB[j] % i == 0:
                    ans.append(arrB[j])
                if arrB[j] % i != 0:
                    num = max(num,i)
            if len(ans) > 0:
                num = 1
        
        if num == 1:
            return 0
        else:
            return num
    
    canDvideA = wantKnow(arrayA)
    canDvideB = wantKnow(arrayB)
    
    resultA = findMaxNum(canDvideA,arrayB)
    resultB = findMaxNum(canDvideB,arrayA)
    
    print(resultA,resultB)
    
    answer = max(resultA,resultB)
     
    return answer
