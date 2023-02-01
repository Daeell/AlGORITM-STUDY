

def solution(arrayA, arrayB):
    answer = 0
    maxi = max(min(arrayA),min(arrayB))
    A=set(arrayA)
    B=set(arrayB)
    if len(list(set(A) - set(B))) != len(A):
        return answer
    A=list(A)
    B=list(B)

    for i in range(maxi,0,-1):
        if A[0] % i == 0 and B[0] % i !=0 :
            for j in A:
                if j% i ==0 and j == A[-1]:
                    for k in B:
                        if k % i !=0 and k ==B[-1]:
                            answer = i
                        elif k% i ==0:
                            break
                elif j% i !=0:
                    break
        else:
            for j in B:
                if j% i ==0 and j == B[-1]:
                    for k in A:
                        if k % i !=0 and k ==A[-1]:
                            answer = i
                        elif k% i ==0:
                            break
                elif j% i !=0:
                    break
        if answer !=0:
            break

    return answer


print(solution([14, 35,119,119,119],[18, 30,102]))