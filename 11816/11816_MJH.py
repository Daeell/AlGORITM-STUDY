X = input()
if len(X) > 2 and X[0] == '0' and X[1] == 'x':
    print(int(X[2:], 16))
elif len(X) > 1 and X[0] == '0':
    print(int(X[1:], 8))
else:
    print(X)