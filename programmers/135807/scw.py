

# def solution(arrayA, arrayB):
#     answer = 0
#     maxi = max(min(arrayA),min(arrayB))
#     A=set(arrayA)
#     B=set(arrayB)
#     if len(list(set(A) - set(B))) != len(A):
#         return answer
#     A=list(A)
#     B=list(B)

#     for i in range(maxi,0,-1):
#         if A[0] % i == 0 and B[0] % i !=0 :
#             for j in A:
#                 if j% i ==0 and j == A[-1]:
#                     for k in B:
#                         if k % i !=0 and k ==B[-1]:
#                             answer = i
#                         elif k% i ==0:
#                             break
#                 elif j% i !=0:
#                     break
#         else:
#             for j in B:
#                 if j% i ==0 and j == B[-1]:
#                     for k in A:
#                         if k % i !=0 and k ==A[-1]:
#                             answer = i
#                         elif k% i ==0:
#                             break
#                 elif j% i !=0:
#                     break
#         if answer !=0:
#             break

#     return answer


def solution(arrayA, arrayB):
    answer =0

    def get_gcd(a,b): # 유클리드 호제법 - 최대공약수 찾기
        if b==0:
            return a
        else:
            return get_gcd(b, a%b)

    def find_gcd(temp_array): # 리스트에서 최대공약수 찾기
        gcd=temp_array[0]
        for i in range(1,len(temp_array)):
            gcd = get_gcd(gcd,temp_array[i])
        return gcd

    Agcd=find_gcd(arrayA)
    Bgcd=find_gcd(arrayB)



    for i in range(len(arrayA)):
        if arrayA[i]%Bgcd !=0 and i == len(arrayA)-1:
            answer = Bgcd
        elif arrayA[i]%Bgcd ==0:
            break
    
    for i in range(len(arrayB)):
        if arrayB[i]%Agcd !=0 and i == len(arrayB)-1:
            answer = max(Agcd, answer)
        elif arrayB[i]%Agcd ==0:
            break

    return answer

print(solution([14, 35,119,119,119],[18, 30,102]))