TRASH = input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
cnt = 0
if len(A) < len(B):
    for n in A:
        if n in B:
            cnt += 1
else:
    for n in B:
        if n in A:
            cnt += 1
print(len(A)+len(B)-cnt*2)