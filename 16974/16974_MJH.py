def burger(level, num) -> int:
    if level == 1:
        if num == 1:
            return 0
        elif 1 < num < 4:
            return num
        else:
            return 3

    tmp = burger(level-1, num)
    


N, X = map(int,input().split())

burger(N, X)