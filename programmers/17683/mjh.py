# 20, 21, 30 실패
def solution(m, musicinfos):
    answer = ''

    # 악보 반음(#) 대체처리
    m = m.replace('C#', 'H')
    m = m.replace('D#', 'I')
    m = m.replace('F#', 'J')
    m = m.replace('G#', 'K')
    m = m.replace('A#', 'L')

    matched_musics = []
    for i in range(len(musicinfos)):
        start_time, end_time, title, musicscore = musicinfos[i].split(',')
        
        # 재생된 시간 산출
        start_h, start_m = map(int, start_time.split(':'))
        end_h, end_m = map(int, end_time.split(':'))
        if start_h < end_h:
            end_m += (end_h - start_h)*60
        duration = end_m - start_m

        # 악보 반음(#) 대체처리
        musicscore = musicscore.replace('C#', 'H')
        musicscore = musicscore.replace('D#', 'I')
        musicscore = musicscore.replace('F#', 'J')
        musicscore = musicscore.replace('G#', 'K')
        musicscore = musicscore.replace('A#', 'L')

        # 재생된 시간에 따라 악보를 자르고 늘림
        if duration < len(musicscore):
            musicscore = musicscore[:duration]
        elif duration > len(musicscore):
            new_musicscore = ''
            for j in range(duration):
                new_musicscore += musicscore[j%len(musicscore)]
            musicscore = new_musicscore
        
        if m in musicscore:
            matched_musics.append([duration, i, title])

    if len(matched_musics) == 0:
        answer = '(None)'
    elif len(matched_musics) == 1:
        answer = matched_musics[0][2]
    else:
        matched_musics.sort(key=lambda x: (x[0], x[1]))
        answer = matched_musics[0][2]

    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))