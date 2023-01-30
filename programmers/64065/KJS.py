def solution(s):
    answer = []
    s_list = list(s)
    remove_set = {'{',','}
    s_list = [i for i in s_list if i not in remove_set]
    print(s_list)
    new_list = []
    for i in s_list:
        if i != '}':
            new_list.append(i)
    print(new_list)
    return answer
