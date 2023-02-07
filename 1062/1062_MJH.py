from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    antic_letters = {'a', 'n', 't', 'i', 'c'}
    letters = []
    alphabet = set()

    N, K = map(int, input().split())

    for i in range(N):
        word = input().strip()[4:-4]
        letters.append(0)
        for letter in word:
            if letter not in antic_letters:
                letters[i] = letters[i] | (1 << (ord(letter)-97))
                alphabet.add(letter)

    if K < 5: return 0
    if len(alphabet) <= K-5: return N

    nCr = combinations(alphabet, K-5)

    maximum = 0
    for case in nCr:
        case_bit = 0
        for letter in case:
            case_bit = case_bit | (1 << (ord(letter)-97))
        cnt = 0
        for i in range(N):
            if (case_bit & letters[i]) == letters[i]:
                cnt += 1
        if maximum < cnt:
            maximum = cnt

    return maximum


print(main())