T = int(input())
A = int(300)
B = int(60)
C = int(10)
if ((T%A)%B)%C >0:
    print(-1)
else:
    answer = [T//A,(T%A)//B,((T%A)%B)//C]
    print(*answer)
