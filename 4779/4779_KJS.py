while True:
    try:

        N = int(input())
        # can = ['-']
        # for i in range(1,3**N):
        #     can[0] = can[0] + '-'


        caN = [0] * (N+1)
        caN[0] = '-'
        for i in range(1, N+1):
            caN[i] = caN[i-1] + ' '*len(caN[i-1]) + caN[i-1]
        print(caN[N])
    except EOFError:
        break
