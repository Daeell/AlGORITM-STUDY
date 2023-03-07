def numCount(x, y, n, arr, zero, one) :
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n) :
            if num != arr[i][j] :
                zero, one = numCount(x, y, n//2, arr, zero, one)
                zero, one = numCount(x, y+n//2, n//2, arr, zero, one)
                zero, one = numCount(x+n//2, y, n//2, arr, zero, one)
                zero, one = numCount(x+n//2, y+n//2, n//2, arr, zero, one)
                return zero, one
    if num == 0 :
        zero += 1
    else : 
        one += 1
    return zero, one

def solution(arr):
    answer = []
    zero = 0
    one = 0
    zero, one = numCount(0, 0, len(arr), arr, zero, one)
    answer.extend([zero, one])
    return answer
