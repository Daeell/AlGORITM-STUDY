def solution(numbers):
    answer = ''
    num_str = list(map(str,numbers))
    num_str.sort(key = lambda x : x*3, reverse = True)
    # print(num_str)
    answer = str(int(''.join(num_str)))
    return answer
