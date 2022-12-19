from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    letters = []
    alphabet = [0]*27
    for i in range(N):
        word = input().strip()
        word = word.replace('a','')
        word = word.replace('n','')
        word = word.replace('t','')
        word = word.replace('i','')
        word = word.replace('c','')

        letters.append(set())

        for letter in word:
            letters[i].add(letter)

        for letter in letters[i]:
            alphabet[ord(letter)-97] += 1

    if K < 5:
        return 0
    
    combinations()
    letters.sort(key=lambda x: len(x))

    i = 0
    while True:

        letters[i]

    print(letters)

    return 0

print(main())