def isSelf(value) :
    for i in range(1, 9*len(str(value)) + 1) :
        num = value - i
        tmp = 0
        if num <= 0 :
            return True
        
        for j in range(len(str(num))) :
            tmp += int(str(num)[j])

        num += tmp
        if num == value :
            return False


n = 10000

for i in range(1, n+1) :
    if isSelf(i) == False :
        pass
    else :
        print(i)

