# PASSED
def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        buf = ''
        compressed_times = 0
        compressed_len = len(s)
        for j in range(0, len(s), i):
            if buf == s[j:i+j]:
                compressed_times += 1
            else:
                if compressed_times != 0:
                    compressed_len -= compressed_times*i
                    compressed_len += len(str(compressed_times+1))
                    compressed_times = 0
                buf = s[j:i+j]
        if compressed_times != 0:
            compressed_len -= compressed_times*i
            compressed_len += len(str(compressed_times+1))
        answer = min(answer, compressed_len)
    
    return answer