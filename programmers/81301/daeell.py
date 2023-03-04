def solution(s):

    words = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
    nums = [str(i) for i in range(10)]
    num = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num += s[i]
            i += 1
        else:
            for j in range(10):
                if s[i:i+len(words[j])] == words[j]:
                    num += nums[j]
                    i += len(words[j])

    return int(num)
