import sys
sys.stdin= open("input.txt", "r")
input= sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
del price[-1]

# 4
# 2 3 1 # 도로의 길이 (N-1개)
# 5 2 4 1 # 가격 

print("거리 :", distance)
print("가격 : ",price)

sorted_price = sorted(price)
print(sorted_price);
end = N-1 ; 
ans = 0 

for i in range(N-1) :
    if price.index(sorted_price[i])>= start  : 
        start = price.index(sorted_price[i]) 
        continue 

    start = price.index(sorted_price[i]) # 제일 저렴한 가격이 가장 먼저 나타나는 도시 
    print("현재 가장 저렴한 가격의 도시 : ",start)
    tmp = 0 
    for j in range (start, end) :
        tmp += distance[j]
    ans += (tmp * sorted_price[i])
    print("현재 총 비용: ",ans)
    end = start
print(ans)

    
    






