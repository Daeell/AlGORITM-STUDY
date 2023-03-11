def solution(n, left, right):
    arr = []
    for i in range(left//n,right//n+1):
        if left//n == right//n:
            for j in range(left%n,right%n+1):
                arr.append(max(i+1,j+1))
        else:
            if i == left//n:
                for j in range(left%n,n):
                    arr.append(max(i+1,j+1))
            elif left // n < i < right//n:
                for j in range(n):
                    arr.append(max(i+1,j+1))
            elif i == right//n:
                for j in range(0,right%n+1):
                    arr.append(max(i+1,j+1))     
    return arr
