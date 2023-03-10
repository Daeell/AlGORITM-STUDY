def solution(skill, skill_trees):
    answer = 0
    
    
    for character in skill_trees :
        return_flag = True    
        check_character = [ x for x in list(character) if x in skill]
        
        for i in range(len(check_character)) :
            if check_character[i] == skill[i%len(skill)] :
                pass
            else :
                return_flag = False
                break

        if return_flag == True :
            answer += 1


    return answer
