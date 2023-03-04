# ALL PASSED
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    string = ""
    while n > 0:
        mod = n%k
        string = str(mod) + string
        n //= k

    cmp = ""
    for i in range(len(string)):
        if string[i] == "0":
            if cmp != "":
                if isPrime(int(cmp)):
                    answer += 1
                cmp = ""
        else:
            cmp += string[i]

    if cmp != "":
        if isPrime(int(cmp)):
            answer += 1

    return answer

print(solution(500000, 3))