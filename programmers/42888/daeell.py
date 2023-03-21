def solution(record):
    users = {}
    for r in record:
        if r.split()[0] in ['Enter', 'Change']:
            users[r.split()[1]] = r.split()[2]

    messages = []

    for r in record:
        if r.split()[0] == 'Enter':
            messages.append(f'{users[r.split()[1]]}님이 들어왔습니다.')
        elif r.split()[0] == 'Leave':
            messages.append(f'{users[r.split()[1]]}님이 나갔습니다.')

    return messages


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
