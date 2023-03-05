# 뭔가 정렬해놓고 붙히면 될 거 같은데 정렬을 어떻게 해야할지 모르겠다
# 3보다 34는 크지만 32는 작게 정렬을 해야하는데 흠..
def solution(numbers):
    answer = ''
    take = []
    store = []
    num = [str(tmp) for tmp in numbers]
    num = sorted(num, key = lambda x : (x[0], len(x)))
    num = [tmp.ljust(4, "A") for tmp in num]
    
    
    print(num)  
    
                
    
    return answer
