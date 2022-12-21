h,m = map(int,input().split())
# 45분 전 
h_flag = False 
d_flag = False

if m>=45 :
    m -= 45
else: 
    h_flag = True
    m += 15

h -= h_flag
if h <0 : 
    h+= 24 

print(h,m)
