def prime_fac(n):
    if n == 1:
        return
    i = 2
    while True:
        if n%i == 0:
            print(i)
            prime_fac(n/i)
            break
        i += 1

N = int(input())
prime_fac (N)