def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill)
    for tree in skill_trees:
        learned = ""
        for s in tree:
            if s in skill_set:
                learned += s
        valid = True
        for i, s in enumerate(learned):
            if s != skill[i]:
                valid = False
                break
        if valid:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
