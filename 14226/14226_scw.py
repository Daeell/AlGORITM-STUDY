#이모티콘
import sys
input=sys.stdin.readline

N = int(input().strip())

sec =0
emo =1
clip = 0
temp_sec =0

def bfs ():
    if N == emo:
        sec = min(sec, temp_sec)
        return sec
    elif emo > N:
        emo -=1
        temp_sec +=1
        bfs()
    else:
        if clip ==0:
            clip = emo
            temp_sec +=1
            bfs()
        else:
            emo +=clip
            temp_sec +=1
            bfs()

