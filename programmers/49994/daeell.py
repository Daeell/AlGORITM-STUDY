def solution(dirs):
    answer = 0
    visited = set()
    x, y = 0, 0

    for dir_ in dirs:
        prev_x, prev_y = x, y
        if dir_ == "U" and y+1 <= 5:
            y += 1
        elif dir_ == "D" and y-1 >= -5:
            y -= 1
        elif dir_ == "R" and x+1 <= 5:
            x += 1
        elif dir_ == "L" and x-1 >= -5:
            x -= 1

        if (prev_x, prev_y) != (x, y) and (x, y, prev_x, prev_y) not in visited and (prev_x, prev_y, x, y) not in visited:
            visited.add((x, y, prev_x, prev_y))
            visited.add((prev_x, prev_y, x, y))
            answer += 1

    return answer


print(solution("ULURRDLLU"))
