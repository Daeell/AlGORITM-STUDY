import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
antatica = set()
antatica.add('a')
antatica.add('n')
antatica.add('t')
antatica.add('i')
antatica.add('c')

alphabet = set()
words =  list()

if K <= 4: 
    print(0)
else:
    for i in range(N) :
        word = input()[4:-5]
        for i in word :
            if i not in antatica :
                alphabet.add(i)
                
    # 가르칠수 있는 글자는 K-5 개 
    print(alphabet)
        
