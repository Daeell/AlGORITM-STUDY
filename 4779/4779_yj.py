import sys
sys.stdin= open("input.txt", "r")
N= sys.stdin.readlines()

def getAnswer(n) :
    if (n == 0) :
        return "-"
    else : 
        frontAndBack = getAnswer(n-1)
        mid = " "* (3**(n-1))
        return frontAndBack + mid + frontAndBack

for i in range(len(N)) :
    N[i] = int(N[i].strip())
    print(getAnswer(N[i]))

